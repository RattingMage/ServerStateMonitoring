import httpx
import asyncio
from celery import shared_task
from asgiref.sync import sync_to_async
from .models import ServerStatus, Server, Incident
from datetime import timedelta
from django.utils.timezone import now


async def fetch_data_from_machine(endpoint):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(endpoint, timeout=10.0)
            return response.json()
        except httpx.RequestError as e:
            print(f"Ошибка при запросе к {endpoint}: {e}")
            return None


async def fetch_all_server_data():
    servers = await sync_to_async(list)(Server.objects.all())
    tasks = {server: fetch_data_from_machine(server.endpoint) for server in servers}

    results = await asyncio.gather(*tasks.values())

    for server, data in zip(tasks.keys(), results):
        if data:
            await sync_to_async(ServerStatus.objects.create)(
                server=server,
                cpu=data['cpu'],
                mem=data['mem'],
                disk=data['disk'],
                uptime=data['uptime']
            )


@shared_task
def fetch_server_data():
    asyncio.run(fetch_all_server_data())

def _create_incident(server, parameter, value):
    existing_incident = Incident.objects.filter(server=server, parameter=parameter, resolved=False).first()
    if not existing_incident:
        Incident.objects.create(
            server=server,
            parameter=parameter,
            value=value,
            start_time=now(),
        )

@shared_task
def check_for_incidents():
    servers = Server.objects.all()
    time_now = now()

    for server in servers:
        cpu_alert_time = time_now - timedelta(minutes=30)
        cpu_statuses = ServerStatus.objects.filter(server=server, timestamp__gte=cpu_alert_time).values_list("cpu", flat=True)
        if cpu_statuses and all(cpu >= 85 for cpu in cpu_statuses):
            _create_incident(server, "CPU", f"{max(cpu_statuses)}%")

        mem_alert_time = time_now - timedelta(minutes=30)
        mem_statuses = ServerStatus.objects.filter(server=server, timestamp__gte=mem_alert_time).values_list("mem", flat=True)
        if mem_statuses and all(int(mem.rstrip('%')) >= 90 for mem in mem_statuses):
            _create_incident(server, "Mem", f"{max(mem_statuses)}%")

        disk_alert_time = time_now - timedelta(hours=2)
        disk_statuses = ServerStatus.objects.filter(server=server, timestamp__gte=disk_alert_time).values_list("disk", flat=True)
        if disk_statuses and all(int(disk.rstrip('%')) >= 95 for disk in disk_statuses):
            _create_incident(server, "Disk", f"{max(disk_statuses)}%")

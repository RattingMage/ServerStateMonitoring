from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Server, ServerStatus, Incident
from .serializers import ServerSerializer, ServerStatusSerializer, IncidentSerializer


class ServerCreateView(generics.CreateAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer


class ServerListView(generics.ListAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer


class ServerStatusView(APIView):
    def get(self, request, pk):
        server = get_object_or_404(Server, pk=pk)
        last_status = ServerStatus.objects.filter(server=server).order_by('-timestamp').first()

        if not last_status:
            return Response({"error": "Нет данных о статусе сервера"}, status=status.HTTP_404_NOT_FOUND)

        return Response(ServerStatusSerializer(last_status).data)


class ServerIncidentsView(APIView):
    def get(self, request, pk):
        server = get_object_or_404(Server, pk=pk)
        incidents = Incident.objects.filter(server=server).order_by('-start_time')
        return Response(IncidentSerializer(incidents, many=True).data)

from django.db import models

class Server(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название сервера")
    endpoint = models.URLField(verbose_name="Эндпоинт сервера")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сервер"
        verbose_name_plural = "Серверы"

class ServerStatus(models.Model):
    server = models.ForeignKey('Server', on_delete=models.CASCADE, verbose_name="Сервер")
    cpu = models.IntegerField(verbose_name="Загрузка CPU (%)")
    mem = models.CharField(max_length=10, verbose_name="Использование памяти")
    disk = models.CharField(max_length=10, verbose_name="Использование диска")
    uptime = models.CharField(max_length=20, verbose_name="Время работы")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Время проверки")

    def __str__(self):
        return f"Статус сервера {self.server.name} на {self.timestamp}"

    class Meta:
        verbose_name = "Статус сервера"
        verbose_name_plural = "Статусы серверов"

class Incident(models.Model):
    server = models.ForeignKey('Server', on_delete=models.CASCADE, verbose_name="Сервер")
    parameter = models.CharField(max_length=50, verbose_name="Параметр")
    value = models.CharField(max_length=20, verbose_name="Значение")
    start_time = models.DateTimeField(verbose_name="Время начала инцидента")
    end_time = models.DateTimeField(null=True, blank=True, verbose_name="Время окончания инцидента")
    resolved = models.BooleanField(default=False, verbose_name="Инцидент разрешён")

    def __str__(self):
        return f"Инцидент на сервере {self.server.name}: {self.parameter} ({self.value})"

    class Meta:
        verbose_name = "Инцидент"
        verbose_name_plural = "Инциденты"

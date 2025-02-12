# Generated by Django 5.1.6 on 2025-02-12 00:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polling', '0002_server'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='serverstatus',
            options={'verbose_name': 'Статус сервера', 'verbose_name_plural': 'Статусы серверов'},
        ),
        migrations.AddField(
            model_name='serverstatus',
            name='server',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='polling.server', verbose_name='Сервер'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='serverstatus',
            name='cpu',
            field=models.IntegerField(verbose_name='Загрузка CPU (%)'),
        ),
        migrations.AlterField(
            model_name='serverstatus',
            name='disk',
            field=models.CharField(max_length=10, verbose_name='Использование диска'),
        ),
        migrations.AlterField(
            model_name='serverstatus',
            name='mem',
            field=models.CharField(max_length=10, verbose_name='Использование памяти'),
        ),
        migrations.AlterField(
            model_name='serverstatus',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время проверки'),
        ),
        migrations.AlterField(
            model_name='serverstatus',
            name='uptime',
            field=models.CharField(max_length=20, verbose_name='Время работы'),
        ),
    ]

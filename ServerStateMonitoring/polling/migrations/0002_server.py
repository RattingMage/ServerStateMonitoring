# Generated by Django 5.1.6 on 2025-02-12 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polling', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название сервера')),
                ('endpoint', models.URLField(verbose_name='Эндпоинт сервера')),
            ],
            options={
                'verbose_name': 'Сервер',
                'verbose_name_plural': 'Серверы',
            },
        ),
    ]

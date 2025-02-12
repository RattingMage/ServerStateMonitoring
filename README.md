# Мониторинг состояния серверов

Проект для мониторинга состояния ресурсов серверов с использованием Django, Celery, Redis и MySQL.

## Описание

Проект позволяет:
- Мониторить состояние ресурсов серверов (CPU, память, диск, время работы).
- Сохранять данные в базу данных MySQL.
- Отображать статусы серверов в панели админа Django.
- Автоматически создавать суперпользователя при запуске контейнера.

## Технологии

- **Python 3.12**
- **Django 5**
- **Celery**
- **Redis**
- **MySQL 8**
- **Docker**

## Установка и запуск

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/RattingMage/amocrm_python_test.git
cd amocrm_python_test/ServerStateMonitoring
```

### 2. Создайте `.env` файл

Создайте `.env` файл и добавьте туда переменные окружения.

Пример модно взять из файла `.env.dev`.

### 3. Запустите проект с помощью Docker Compose

```bash
docker-compose up --build
```

### 4. Доступ к проекту

 - Django-приложение: http://localhost:8000
 - Админка Django: http://localhost:8000/admin
   - Логин: `admin`
   - Пароль: `adminpassword`

## Тестирование

Для эмуляции данных серверов, можно поднять приложение на FastAPI.

### 1.Создать и активировать виртуальеое окружение Python

```bash
cd amocrm_python_test/mock_server
py -m venv .\venv
```
```bash
.\venv\Scripts\activate
```

### 2.Установить зависимости

```bash
pip install -r .\requirements.txt
```

### 3.Запустить приложение

```bash
python main.py
```

### 4.Доступ к серверу

- http://<host_ip>:8001/api/status/1
- http://<host_ip>:8001/api/status/2
- http://<host_ip>:8001/api/status/3

Где host_ip IP-адрес хоста
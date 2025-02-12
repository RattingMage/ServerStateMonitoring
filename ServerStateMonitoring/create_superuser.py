import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ServerStateMonitoring.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

def create_superuser():
    username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')
    email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
    password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'adminpassword')

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)
        print(f"Суперпользователь {username} создан.")
    else:
        print(f"Суперпользователь {username} уже существует.")

if __name__ == '__main__':
    create_superuser()
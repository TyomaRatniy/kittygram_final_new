import pytest
import os
import django

def pytest_configure():
    """Настройка pytest для использования тестовых настроек"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_settings')

@pytest.fixture(scope='session', autouse=True)
def django_setup():
    """Настройка Django для тестов"""
    django.setup()

@pytest.mark.django_db
def test_database_connection():
    """Тест подключения к базе данных"""
    from django.db import connection
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
    
    assert result[0] == 1
    print("✅ База данных подключена успешно")

def test_basic():
    """Базовый тест без БД"""
    assert 1 + 1 == 2

def test_django_available():
    """Тест что Django работает (без БД)"""
    from django.conf import settings
    assert settings.SECRET_KEY is not None
    assert hasattr(settings, 'DATABASES')
    print("✅ Django настроен корректно")

@pytest.mark.django_db
def test_create_test_data():
    """Тест создания тестовых данных"""
    from django.contrib.auth.models import User
    
    # Создаем тестового пользователя
    user = User.objects.create_user(
        username='testuser',
        email='test@example.com',
        password='testpass123'
    )
    
    assert user.id is not None
    assert User.objects.filter(username='testuser').exists()
    print(f"✅ Тестовый пользователь создан: {user.username}")

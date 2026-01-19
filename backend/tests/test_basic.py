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

def test_database_connection():
    """Тест подключения к базе данных"""
    from django.db import connection
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
    
    assert result[0] == 1
    print("✅ База данных подключена успешно")

def test_basic():
    """Базовый тест"""
    assert 1 + 1 == 2

def test_django_available():
    """Тест что Django работает"""
    from django.conf import settings
    assert settings.SECRET_KEY is not None
    assert hasattr(settings, 'DATABASES')
    print("✅ Django настроен корректно")

import pytest
import os
import django

@pytest.fixture(scope='session')
def django_db_setup():
    """Настройка Django для тестов"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kittygram_backend.settings')
    django.setup()

def test_database_connection(django_db_setup):
    """Тест подключения к базе данных"""
    from django.db import connection
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
    
    assert result[0] == 1
    print("✅ База данных подключена успешно")

def test_create_user(django_db_setup):
    """Тест создания пользователя"""
    from django.contrib.auth.models import User
    
    # Удаляем тестового пользователя если существует
    User.objects.filter(username='testuser').delete()
    
    # Создаем пользователя
    user = User.objects.create_user(
        username='testuser',
        password='testpassword123',
        email='test@example.com'
    )
    
    assert user.id is not None
    assert user.username == 'testuser'
    assert user.check_password('testpassword123')
    
    # Проверяем что пользователь сохранился в БД
    user_count = User.objects.filter(username='testuser').count()
    assert user_count == 1
    
    print(f"✅ Пользователь создан: {user.username}")

def test_basic_math():
    """Простой математический тест"""
    assert 1 + 1 == 2
    assert 2 * 2 == 4

import pytest

def test_basic():
    assert 1 + 1 == 2

@pytest.mark.django_db
def test_django_db():
    from django.contrib.auth.models import User
    user = User.objects.create_user(username='test', password='test')
    assert User.objects.count() == 1

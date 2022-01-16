import pytest
from django.contrib.auth import get_user_model
from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.fixture
def user_data():
    return {'username': 'user_test', 'first_name': 'user_first_name',
            'last_name': 'user_last_name', 'email': 'user_email@user.com', 'password': 'password'}


@pytest.fixture
def profile_data():
    return {'user': 'user_test', 'favorite_city': 'london'}


@pytest.fixture
def create_test_user(user_data):
    user_model = get_user_model()
    test_user = user_model.objects.create_user(**user_data)
    test_user.set_password(user_data.get('password'))
    return test_user


@pytest.fixture
def create_test_profile(profile_data):
    user = User.objects.get(username=profile_data.get('user'))
    profile = Profile.objects.create(user=user, favorite_city=profile_data.get('favorite_city'))
    return profile

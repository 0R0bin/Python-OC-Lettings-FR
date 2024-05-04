import pytest

from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_profiles_model():

    profile = Profile.objects.create(
               user=User.objects.create(username='test_user_profile'),
               favorite_city="Cannes"
               )

    expected_value = "test_user_profile"
    assert str(profile) == expected_value

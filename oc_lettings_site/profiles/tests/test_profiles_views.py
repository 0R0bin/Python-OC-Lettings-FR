import pytest

from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse
from profiles.models import Profile
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_profiles_index_view():
    """Test of the index view of profiles"""

    client = Client()

    path = reverse('profiles:index')
    response = client.get(path)
    content = response.content.decode()

    assert response.status_code == 200
    assert '<h1 class="page-header-ui-title mb-3 display-6">Profiles</h1>' in content
    assertTemplateUsed(response, r'profiles/index.html')


@pytest.mark.django_db
def test_profiles_details_view():
    """Test of the details view of profiles"""

    client = Client()

    profile = Profile.objects.create(
               user=User.objects.create(username='test_user_profile'),
               favorite_city="Cannes"
               )

    username = profile.user.username

    path = reverse('profiles:profile', kwargs={'username': username})
    response = client.get(path)
    content = response.content.decode()

    div_to_find = '<h1 class="page-header-ui-title mb-3 display-6">' + username + '</h1>'

    assert response.status_code == 200
    assert div_to_find in content
    assertTemplateUsed(response, r'profiles/profile.html')

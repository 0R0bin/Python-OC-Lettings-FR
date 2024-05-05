import pytest

from lettings.models import Address
from lettings.models import Letting
from django.test import Client
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_lettings_index_view():
    """Test of the index view of lettings"""

    client = Client()

    path = reverse('lettings:index')
    response = client.get(path)
    content = response.content.decode()

    assert response.status_code == 200
    assert '<h1 class="page-header-ui-title mb-3 display-6">Lettings</h1>' in content
    assertTemplateUsed(response, r'lettings/index.html')


@pytest.mark.django_db
def test_lettings_details_view():
    """Test of the details view of lettings"""

    client = Client()

    address = Address.objects.create(
               number=6,
               street='Soutrane',
               city='Valbonne',
               state='France',
               zip_code='06520',
               country_iso_code='FR')

    letting = Letting.objects.create(
               title='Letting_Test',
               address=address
               )

    path = reverse('lettings:letting', kwargs={'letting_id': 1})
    response = client.get(path)
    content = response.content.decode()

    div_to_find = '<h1 class="page-header-ui-title mb-3 display-6">' + letting.title + '</h1>'

    assert response.status_code == 200
    assert div_to_find in content
    assertTemplateUsed(response, r'lettings/letting.html')

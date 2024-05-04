import pytest

from django.test import Client
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_lettings_index_view():
    """Test of the index view of base"""

    client = Client()

    path = reverse('lettings:index')
    response = client.get(path)
    content = response.content.decode()

    assert response.status_code == 200
    assert '<h1 class="page-header-ui-title mb-3 display-6">Lettings</h1>' in content
    assertTemplateUsed(response, r'lettings/index.html')

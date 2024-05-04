import pytest

from django.test import Client
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


def test_lettings_index_view():
    """Test of the index view of base"""

    URL = r'lettings:index'
    path = reverse(URL)
    client = Client()
    response = client.get(path)
    content = response.content.decode()

    assert response.status_code == 200
    assert '<h1>Lettings</h1>' in content
    assertTemplateUsed(response, r'lettings/index.html')

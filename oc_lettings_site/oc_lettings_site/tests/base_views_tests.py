from django.test import Client
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


def test_base_index_view():
    """Test of the index view of base"""

    URL = r'index'
    path = reverse(URL)
    client = Client()
    response = client.get(path)
    content = response.content.decode()

    assert '<h1 class="page-header-ui-title mb-3 display-6">Welcome to Holiday Homes</h1>' in content
    assert response.status_code == 200
    assertTemplateUsed(response, r'oc_lettings_site/index.html')


def test_404_view():
    """Test of the 404 view"""
    PATH = r'unkonw_addr'
    client = Client()
    response = client.get(PATH)
    content = response.content.decode()

    assert '<h1>Oops! Page Not Found</h1>' in content
    assert response.status_code == 404
    assertTemplateUsed(response, r'oc_lettings_site/404.html')
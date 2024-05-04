from django.test import Client
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


def test_home_index_view():
    """ Test of the index view of base """

    URL = r'index'
    path = reverse(URL)
    client = Client()
    response = client.get(path)
    content = response.content.decode()

    print(URL)
    print(content)

    assert '<h1 class="page-header-ui-title mb-3 display-6">Welcome to Holiday Homes</h1>' in content
    assert response.status_code == 200
    assertTemplateUsed(response, "oc_lettings_site/index.html")
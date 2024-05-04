from django.urls import reverse, resolve


def test_home_index_url():
    """Test of the index URL """

    URL = r'index'
    path = reverse(URL)
    result = resolve(path)

    assert path == '/'
    assert result.view_name == 'index'
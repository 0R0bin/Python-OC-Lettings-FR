from django.urls import reverse, resolve


def test_base_index_url():
    """Test of the index URL """

    URL = r'index'
    path = reverse(URL)
    result = resolve(path)

    assert path == r'/'
    assert result.view_name == r'index'
from django.urls import reverse, resolve


def test_profiles_index_url():
    """Test of the letting index URL"""

    URL = r'profiles:index'
    path = reverse(URL)
    result = resolve(path)

    assert path == r'/profiles/'
    assert result.view_name == URL


def test_profiles_details_url():
    """Test of the letting details URL"""

    URL = r'profiles:profile'
    path = reverse(URL, args=['test_str'])
    result = resolve(path)

    assert path == r'/profiles/test_str/'
    assert result.view_name == URL
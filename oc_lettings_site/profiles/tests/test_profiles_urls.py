from django.urls import reverse, resolve


def test_profiles_index_url():
    """Test of the letting index URL"""

    VIEW_NAME = 'profiles:index'
    path = reverse(VIEW_NAME)
    result = resolve(path)

    assert path == r'/profiles/'
    assert result.view_name == VIEW_NAME


def test_profiles_details_url():
    """Test of the letting details URL"""

    VIEW_NAME = 'profiles:profile'
    path = reverse(VIEW_NAME, kwargs={'username': 'test_str'})
    result = resolve(path)

    assert path == r'/profiles/test_str/'
    assert result.view_name == VIEW_NAME

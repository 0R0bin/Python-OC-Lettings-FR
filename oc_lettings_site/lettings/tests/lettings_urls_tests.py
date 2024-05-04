from django.urls import reverse, resolve


def test_letting_index_url():
    """Test of the lettings_app index URL"""

    URL = r'lettings:index'
    path = reverse(URL)
    result = resolve(path)

    assert path == r'/lettings/'
    assert result.view_name == 'lettings:index'


def test_letting_details_url():
    """Test of the lettings_app details URL"""

    URL = r'lettings:letting'
    path = reverse(URL, args=[1])
    result = resolve(path)

    assert path == r'/lettings/1/'
    assert result.view_name == 'lettings:letting'
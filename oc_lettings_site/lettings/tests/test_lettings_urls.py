from django.urls import reverse, resolve


def test_lettings_index_url():
    """Test of the lettings_app index URL"""

    VIEW_NAME = 'lettings:index'
    path = reverse(VIEW_NAME)
    result = resolve(path)

    assert path == r'/lettings/'
    assert result.view_name == VIEW_NAME


def test_lettings_details_url():
    """Test of the lettings_app details URL"""

    VIEW_NAME = 'lettings:letting'
    path = reverse(VIEW_NAME, kwargs={'letting_id': 1})
    result = resolve(path)

    assert path == r'/lettings/1/'
    assert result.view_name == VIEW_NAME

from django.urls import reverse, resolve


def test_base_index_url():
    """Test of the index URL """

    VIEW_NAME = 'index'
    path = reverse(VIEW_NAME)
    result = resolve(path)

    assert path == r'/'
    assert result.view_name == VIEW_NAME

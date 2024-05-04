import pytest

from lettings.models import Address
from lettings.models import Letting


@pytest.mark.django_db
def test_lettings_models():
    """Test the Letting Models with __str__"""

    address = Address.objects.create(
               number=6,
               street='Soutrane',
               city='Valbonne',
               state='France',
               zip_code='06520',
               country_iso_code='FR')

    letting = Letting.objects.create(
               title='Letting_Test',
               address=address
               )

    expected_value_address = '6 Soutrane'
    expected_value_letting = 'Letting_Test'
    assert str(address) == expected_value_address
    assert str(letting) == expected_value_letting

from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db import models


class Address(models.Model):
    """Model used for Addresses"""
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        db_table = 'oc_lettings_site_address'
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """Model used for Letting, using PrimaryKey to Address"""
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    class Meta:
        db_table = 'oc_lettings_site_letting'
        verbose_name = "Letting"
        verbose_name_plural = "Lettings"

    def __str__(self):
        return self.title

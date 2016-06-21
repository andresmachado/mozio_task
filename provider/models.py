from django.contrib.auth.models import User
from django.contrib.gis.db import models


class Provider(models.Model):
    user = models.ForeignKey(User, related_name='provider')
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20)
    language = models.CharField(max_length=150)
    currency = models.CharField(max_length=3)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Providers'


class Polygon(models.Model):
    provider = models.ForeignKey(Provider, related_name='polygons')
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    poly = models.PolygonField()

    def __str__(self):
        return self.name

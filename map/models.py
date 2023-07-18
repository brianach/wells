from django.db import models


class Well(models.Model):
    well = models.CharField(max_length=100)
    townland = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    longitude = models.DecimalField(max_digits=8, decimal_places=4)
    latitude = models.DecimalField(max_digits=8, decimal_places=4)
    cures = models.CharField(max_length=100)

    def __str__(self):
        return self.well

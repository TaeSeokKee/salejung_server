from django.db import models

# Create your models here.

# Todo : image upload path will be specific date.
class Photo(models.Model):
    userId = models.CharField(max_length=50, blank=False)
    photoFilePath = models.CharField(max_length=200, blank=False)
    detail = models.CharField(max_length=200, blank=False)
    date = models.CharField(max_length=100, blank=False)
    lat = models.DecimalField(max_digits=9, decimal_places=6, blank=False)
    lng = models.DecimalField(max_digits=9, decimal_places=6, blank=False)
    address = models.CharField(max_length=100, blank=False)
    country = models.CharField(max_length=10, blank=False)
    topic = models.CharField(max_length=20, blank=False)


    class Meta:
        # lng index and next lat index is more efficient.
        indexes = [
            models.Index(fields=['lng', 'lat'])
        ]


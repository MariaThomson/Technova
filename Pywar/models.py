from django.db import models

# Create your models here.
class Pywar(models.Model):
    title = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=150, blank=False)
    registration_fees = models.IntegerField(default=0)
    expense = models.IntegerField(default=0)

    def __str__(self):
        return self.title
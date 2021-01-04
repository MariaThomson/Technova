from django.db import models
from Pywar.models import Pywar
# Create your models here.

class registration(models.Model):
    event = models.ForeignKey(Pywar,on_delete=models.CASCADE)
    name_of_the_participant = models.CharField(max_length=50, blank=False)
    college = models.CharField(max_length=50, blank=False)
    branch = models.CharField(max_length=50, blank=False)
    semester = models.IntegerField(default=0)
    

    def __str__(self):
        return self.name_of_the_participant
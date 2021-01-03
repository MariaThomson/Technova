from django.db import models

# Create your models here.

class registration(models.Model):
    title = models.CharField(max_length=50, blank=False)
    name_of_the_participant = models.CharField(max_length=50, blank=False)
    college = models.CharField(max_length=50, blank=False)
    branch = models.CharField(max_length=50, blank=False)
    semester = models.IntegerField(default=0)
    

    def __str__(self):
        return self.title
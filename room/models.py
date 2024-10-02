from django.db import models
from equipment.models import Equipment

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    location = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    equipments = models.ManyToManyField(Equipment, blank=True)
    photo = models.ImageField(upload_to='room_photos', blank=True, null=True)

    def __str__(self):
        return self.name
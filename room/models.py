from django.db import models
from equipment.models import Equipment
from django.contrib.auth.models import User
from django.db.models import Avg


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    location = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    equipments = models.ManyToManyField(Equipment, blank=True)
    photo = models.ImageField(upload_to='room_photos', blank=True, null=True)

    def average_rating(self):
        return self.ratings.aggregate(Avg('score'))['score__avg'] or 0
    
    def __str__(self):
        return self.name


class Rating(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.room.name} - {self.user.username} - {self.score}'
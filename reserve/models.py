from django.contrib.auth.models import User
from django.db import models
from room.models import Room


# Create your models here.
class Reserve(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')

    def __str__(self):
        return f'{self.user.username} - {self.room.name} ({self.date})'
    
    class Meta:
        ordering = ['date']
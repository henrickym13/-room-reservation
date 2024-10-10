from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now
from datetime import timedelta
from .models import Reserve
from .utils import email_send


@receiver(post_save, sender=Reserve)
def send_reservation_reminder(sender, instance, **kwargs):
    if instance.status == 'confirmada':
        reserve_date = instance.date
        date_now = now().date()

        if reserve_date - date_now == timedelta(days=1):
            title = 'Lembrete de Reserva'
            message = f'Lembre-se de que você tem uma reserva da sala {instance.room.name} amanhã às {instance.start_time}.'
            recipients = [instance.user.email]
            email_send(title, message, recipients)
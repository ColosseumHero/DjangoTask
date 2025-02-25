from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from events.models import Event

@receiver(post_save, sender=Event)
def send_event_created_email(sender, instance, created, **kwargs):
    if created and instance.user:
        subject = f"Event Created: {instance.title}"
        message = f"Dear {instance.user.username},\n\nYour event '{instance.title}' has been successfully created!\n\nThank you!"
        print(f"Dear {instance.user.username},\n\nYour event '{instance.title}' has been successfully created!\n\nThank you!")
        recipient_email = instance.user.email
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient_email])




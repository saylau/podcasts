import uuid
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from fcm_django.models import FCMDevice

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.username

class Notification(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    body = models.CharField(max_length=250, verbose_name='Текст')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'

    def save(self, *args, **kwargs):
        if not self.pk:
            device = FCMDevice.objects.all()
            data = {
                'title': notification.title,
                'body': notification.body
            }
            device.send_message(title=notification.title, body=notification.body, data=data, sound="default")
        super(Notification, self).save(*args, **kwargs)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

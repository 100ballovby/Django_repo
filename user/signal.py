from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Profile


# получатель(данные_формы, модель_пользователя)
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:  # если статус "создан" = True
        Profile.objects.create(user=instance)  # Модель.объекты.создать(за юзера взять сущность БД)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

"""
post_save - это сигнал, которые будет отправляться при окончании работы 
метода "сохранения"
"""


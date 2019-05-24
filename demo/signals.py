from django.db.models import Max
from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import User


@receiver(pre_save, sender=User)
def create_email(sender, instance, *args, **kwargs):
    # checks if user has an account number
    if not instance.email:
        # gets the largest account number
        largest = User.objects.all().aggregate(
            Max("email")
            )['email__max']

        if largest:
            # creates new account number
            instance.email = largest + 1
        else:
            # if there is no other user, sets users account number to 10000000.
            instance.email = 10000000

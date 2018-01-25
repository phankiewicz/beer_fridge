import json
import requests

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Beer


@receiver(post_save, sender=Beer)
def create_user_profile(sender, instance, created, **kwargs):
    temp = instance.current_temperature or 20
    if temp <= instance.type.serving_temperature:
        url = 'https://hooks.zapier.com/hooks/catch/2773929/8jze1o/'
        payload = {'beer': 'ready'}
        headers = {'content-type': 'application/json'}

        r = requests.post(url, data=json.dumps(payload), headers=headers)

#Question 3: By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

'''Yes,  Django signals run in the same database transaction as the caller. This means that if a signal is sent during a database operation, the signal handlers will execute in the same transaction context, and if the transaction is rolled back, the actions performed by the signal handlers will also be rolled back.'''

#example
from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_model_post_save(sender, instance, created, **kwargs):
   
    if created:
        raise ValidationError("Simulating an error after save.")


def create_my_model_instance():
    try:
        with transaction.atomic():
            my_instance = MyModel(name="Test Instance")
            my_instance.save()  
    except ValidationError as e:
        print(f"Transaction rolled back due to error: {e}")

create_my_model_instance()

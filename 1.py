#Question 1: By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

#answer : 
''' Django signals are executed synchronously, meaning that the signal handlers are executed in the same thread and process that triggered the signal, and they block further execution until they complete.'''

# Below is the example

# models.py
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import time

class MyModel(models.Model):
    name = models.CharField(max_length=100)

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal handler started")
    time.sleep(5)  
    print("Signal handler finished")


from myapp.models import MyModel   #myapp is the application name
import time

start_time = time.time()

instance = MyModel.objects.create(name='Test Instance')
end_time = time.time()
print(f"Total time taken: {end_time - start_time} seconds")

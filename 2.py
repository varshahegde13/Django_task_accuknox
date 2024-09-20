#Question 2: Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

'''Yes, Django signals run in the same thread as the caller. When a signal is sent, any connected signal handlers are executed in the context of the thread that sent the signal.'''

#example 

from django.dispatch import Signal, receiver
import threading
import time

my_signal = Signal()

@receiver(my_signal)
def my_handler(sender, **kwargs):
    print(f"Signal received in thread: {threading.current_thread().name}")

def emit_signal():
    print(f"Emitting signal in thread: {threading.current_thread().name}")
    my_signal.send(sender=None)

if __name__ == "__main__": 
    thread = threading.Thread(target=emit_signal)
    thread.start()
    thread.join()  
from django.dispatch import Signal

signal_name = Signal(providing_args=["user",])

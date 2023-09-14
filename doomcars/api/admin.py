from django.contrib import admin
from .models import *

# List of models to register
models_to_register = [Profile, Car, Booking, Payment, Location, Review, Notification, Discount]

# Define a function to register models
def register_models(models):
    for model in models:
        admin.site.register(model)

# Register the models
register_models(models_to_register)
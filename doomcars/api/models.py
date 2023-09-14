from django.db import models
from django.contrib.auth.models import User
import uuid
class Profile(models.Model):
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Add additional fields like phone number, driver's license, etc.

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    license_plate = models.CharField(max_length=20)
    available=models.BooleanField(default=True)
    location=models.ForeignKey(to='Location',on_delete=models.CASCADE)
    # Add more fields like photos, description, availability status, etc.

class Booking(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
   

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_id = models.UUIDField(default=uuid.uuid4,max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    # Add availability status and other location-related fields

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comments = models.TextField()

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Discount(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount_amount = models.DecimalField(max_digits=5, decimal_places=2)
    expiration_date = models.DateField()

# Implement the rest of the models (Feedback, Reservation, Transaction, Insurance, Maintenance, CarOwner) in a similar fashion.

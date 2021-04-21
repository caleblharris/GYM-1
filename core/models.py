from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    gender_name = models.TextField
    email_name = models.TextField()
    phone_number = models.IntegerField()
    address_number = models.IntegerField()
    address_name = models.TextField()
    instructor_name = models.TextField()

class Profile(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    gender_name = models.TextField
    email_name = models.TextField()
    phone_number = models.IntegerField()
    address_number = models.IntegerField()
    address_name = models.TextField()
    password_name = models.TextField()
    

class Memberships(models.Model):
    memberships_name = models.IntegerField()
    memberships_payment = models.IntegerField()
    memberships_duration = models.IntegerField()
    status_name = models.TextField()

    
class Journal(models.Model):
    memberships_id = models.TextField()
    workout_id = models.TextField()
    check_in_date = models.IntegerField()
    check_in_time = models.IntegerField()
    check_out_time = models.IntegerField()
    instructor_name = models.TextField()
        
class Workout(models.Model):
    workout_name = models.TextField()
    workout_description = models.TextField()
    

class Instructor(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    gender_name = models.TextField
    email_name = models.TextField()
    phone_number = models.IntegerField()
           
class Payment(models.Model):
    person_name = models.TextField()
    payment_date = models.IntegerField()
    payment_amount = models.IntegerField()
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.TextField(max_length=200, null=True)
    last_name = models.TextField(max_length=200, null=True)
    gender_name = models.TextField(max_length=200, null=True)
    email_name = models.TextField(max_length=200, null=True)
    phone_number = models.IntegerField(max_length=200, null=True)
    address_number = models.IntegerField(max_length=200, null=True)
    address_name = models.TextField(max_length=200, null=True)
    instructor_name = models.TextField(max_length=200, null=True)

def __str__(self):
		return self.name

class Profile(models.Model):
    first_name = models.TextField(max_length=200, null=True)
    last_name = models.TextField(max_length=200, null=True)
    gender_name = models.TextField(max_length=200, null=True)
    email_name = models.TextField(max_length=200, null=True)
    phone_number = models.IntegerField(max_length=200, null=True)
    address_number = models.IntegerField(max_length=200, null=True)
    address_name = models.TextField(max_length=200, null=True)
    password_name = models.TextField(max_length=200, null=True)

def __str__(self):
		return self.name  
    

class Memberships(models.Model):
    memberships_name = models.IntegerField(max_length=200, null=True)
    memberships_payment = models.IntegerField(max_length=200, null=True)
    memberships_duration = models.IntegerField(max_length=200, null=True)
    status_name = models.TextField(max_length=200, null=True)

def __str__(self):
		return self.name  

    
class Journal(models.Model):
    memberships_id = models.TextField(max_length=200, null=True)
    workout_id = models.TextField(max_length=200, null=True)
    check_in_date = models.IntegerField(max_length=200, null=True)
    check_in_time = models.IntegerField(max_length=200, null=True)
    check_out_time = models.IntegerField(max_length=200, null=True)
    instructor_name = models.TextField(max_length=200, null=True)

def __str__(self):
		return self.name  
        
class Workout(models.Model):
    workout_name = models.TextField(max_length=200, null=True)
    workout_description = models.TextField(max_length=200, null=True)

def __str__(self):
		return self.name   
    

class Instructor(models.Model):
    first_name = models.TextField(max_length=200, null=True)
    last_name = models.TextField(max_length=200, null=True)
    gender_name = models.TextField(max_length=200, null=True)
    email_name = models.TextField(max_length=200, null=True)
    phone_number = models.IntegerField(max_length=200, null=True)

def __str__(self):
		return self.name
           
class Payment(models.Model):
    person_name = models.TextField(max_length=200, null=True)
    payment_date = models.IntegerField(max_length=200, null=True)
    payment_amount = models.FloatField(null=True)

def __str__(self):
		return self.name
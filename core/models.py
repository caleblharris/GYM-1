from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class Instructor(models.Model):
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address_name = models.CharField(max_length=200, null=True, blank=True)
    instructor_name = models.ForeignKey(Instructor, on_delete=models.PROTECT, null=True, blank=True)


def __str__(self):
    return self.first_name 

class Memberships(models.Model):
    memberships_name = models.CharField(max_length=200, null=True, blank=True)
    memberships_payment = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    memberships_duration = models.IntegerField(null=True, blank=True)
    status_name = models.CharField(max_length=200, null=True, blank=True)

def __str__(self):
	    return self.name  

class Workout(models.Model):
    workout_name = models.TextField(max_length=200, null=True, blank=True)
    workout_description = models.TextField(max_length=200, null=True, blank=True)

def __str__(self):
	    return self.name   

class Journal(models.Model):
    membership = models.ForeignKey(Memberships, on_delete=models.PROTECT, null=True, blank=True)
    workout = models.ForeignKey(Workout, on_delete=models.PROTECT, null=True, blank=True)
    check_in_datetime = models.DateTimeField(null=True, blank=True)
    check_out_datetime = models.DateTimeField(null=True, blank=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.PROTECT, null=True, blank=True)

def __str__(self):
	    return self.name  
           
class Payment(models.Model):
    person_name = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True, blank=True)
    payment_date = models.DateField(null=True, blank=True)
    payment_amount = models.FloatField(null=True)

def __str__(self):
	    return self.name
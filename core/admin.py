from django.contrib import admin

# Register your models here.

from core.models import *

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    search_fields = [ 'first_name', 'last_name']
    list_display = ('first_name', 'last_name', 'gender', 'email','phone_number','address_name','memberships_name','instructor_name')

@admin.register(Memberships)
class MembershipsAdmin(admin.ModelAdmin):
    pass

@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    pass

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    pass

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    pass

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass
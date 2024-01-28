from django.db import models

class BloodInventory(models.Model):
    blood_group = models.CharField(max_length=2)  # Assuming only A, B, AB, O without +/-
    quantity_liters = models.IntegerField(default=0)

class Patient(models.Model):
    name = models.CharField(max_length=255)
    blood_group = models.CharField(max_length=2)
    blood_required_liters = models.IntegerField()
    days_in_hospital = models.IntegerField()

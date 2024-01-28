from django.db import models

class Bed(models.Model):
    occupied = models.BooleanField(default=False)
    patient_name = models.CharField(max_length=255, blank=True, null=True)

class Patient(models.Model):
    name = models.CharField(max_length=255)

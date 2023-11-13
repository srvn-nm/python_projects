from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    national_code = models.CharField(max_length=10, unique=True)
    ip_address = models.GenericIPAddressField()
    username = models.CharField(max_length=100, unique=True)
    image1 = models.CharField(max_length=10000000)
    image2 = models.CharField(max_length=10000000)
    state_types = (
        (0, "Denied"),
        (1, "InProgress"),
        (2, "Accepted"),
    )
    state = models.IntegerField(choices=state_types, default=0)

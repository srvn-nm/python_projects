from enum import IntEnum
from rest_framework import serializers
from django.utils.text import slugify
import random
import string
from API.models import User
import requests


class State(IntEnum):
    DENIED = 0
    IN_PROGRESS = 1
    ACCEPTED = 2

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]



def encrypt_national_code(national_code):
    encrypted_id = national_code[::-1]  # Reverse the national ID
    return encrypted_id


def decrypt_national_id(encrypted_id):
    decrypted_id = encrypted_id[::-1]  # Reverse the encrypted ID
    return decrypted_id



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'




def generate_unique_username(name, email):
    # Create a username based on the user's name or email
    # You can modify this logic to suit your requirements
    base_username = slugify(name or email.split('@')[0])

    # Append a random string to ensure uniqueness
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
    username = f"{base_username}-{random_string}"

    # Ensure the username is unique
    Username = User.__class__
    while Username.objects.filter(username=username).exists():
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
        username = f"{base_username}-{random_string}"

    return username



def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def save_user_images(username, image1, image2):
    api_key = '&lt;replace-with-your-api-key&gt;'
    api_secret ='6ad87a8557035262199de5efafb5786b'
    response = requests.post(
        'https://api.imagga.com/v2/tags',
        auth=(api_key, api_secret),
        files={'image1': open(image1, 'rb')})
    print(response.json())
    response2 = requests.post(
        'https://api.imagga.com/v2/tags',
        auth=(api_key, api_secret),
        files={'image2': open(image2, 'rb')})
    print(response2.json())
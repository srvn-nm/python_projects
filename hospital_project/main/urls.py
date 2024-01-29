from django.urls import path, include

from main.views import main

urlpatterns = [
    path('reception/', include('reception.urls')),
    path('blood_bank/', include('blood_bank.urls')),
    path('', main, name='main_view'),
]

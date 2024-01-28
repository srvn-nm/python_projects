from django.urls import path, include

urlpatterns = [
    path('reception/', include('reception.urls')),
    path('blood_bank/', include('blood_bank.urls')),
]

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reception/', include('reception.urls')),
    path('blood_bank/', include('blood_bank.urls')),
    # Add other app URLs here
]

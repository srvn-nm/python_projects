from django.urls import path
from .views import set_blood_bank, add_to_blood_bank, add_patient, is_critical_mode_on

urlpatterns = [
    path('set_blood_bank/', set_blood_bank, name='set_blood_bank'),
    path('add_to_blood_bank/', add_to_blood_bank, name='add_to_blood_bank'),
    path('add_patient/', add_patient, name='add_patient'),
    path('is_critical_mode_on/', is_critical_mode_on, name='is_critical_mode_on'),
]

from django.urls import path
from .views import set_total_beds, admit_patient, get_empty_beds, discharge_patient

urlpatterns = [
    path('set_total_beds/', set_total_beds, name='set_total_beds'),
    path('admit_patient/', admit_patient, name='admit_patient'),
    path('get_empty_beds/', get_empty_beds, name='get_empty_beds'),
    path('discharge_patient/', discharge_patient, name='discharge_patient'),
]

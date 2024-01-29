# from django.db.models import Sum
from django.shortcuts import render
# from reception.models import Bed
# from blood_bank.models import BloodInventory, Patient


def main(request):
    # Fetch relevant data for the system overview
    # total_beds = Bed.objects.count()
    # empty_beds = Bed.objects.filter(patient__isnull=True).count()
    # total_blood_liters = BloodInventory.objects.aggregate(total=Sum('blood_liters'))['total']
    # total_patients = Patient.objects.count()

    # context = {
    #     'total_beds': total_beds,
    #     'empty_beds': empty_beds,
    #     'total_blood_liters': total_blood_liters,
    #     'total_patients': total_patients,
    # }

    return render(request, 'main/main_page.html')
    # , context)

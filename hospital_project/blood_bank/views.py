from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET, require_http_methods  # تغییر این خط

from .models import BloodInventory, Patient

@csrf_exempt
@require_POST
def set_blood_bank(request):
    blood_group = request.POST.get('blood_group', '')
    quantity_liters = int(request.POST.get('quantity_liters', 0))

    try:
        BloodInventory.objects.create(blood_group=blood_group, quantity_liters=quantity_liters)
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

@csrf_exempt
@require_http_methods(["PUT"])
def add_to_blood_bank(request):
    blood_group = request.POST.get('blood_group', '')
    quantity_change = int(request.POST.get('quantity_change', 0))

    try:
        blood_inventory = BloodInventory.objects.get(blood_group=blood_group)
        blood_inventory.quantity_liters += quantity_change
        blood_inventory.save()

        # Check and update critical mode status
        check_and_update_critical_mode()

        return JsonResponse({'success': True})
    except BloodInventory.DoesNotExist:
        return JsonResponse({'success': False})

@csrf_exempt
@require_POST
def add_patient(request):
    patient_name = request.POST.get('patient_name', '')
    blood_group = request.POST.get('blood_group', '')
    blood_required_liters = int(request.POST.get('blood_required_liters', 0))
    days_in_hospital = int(request.POST.get('days_in_hospital', 0))

    try:
        patient = Patient.objects.create(
            name=patient_name,
            blood_group=blood_group,
            blood_required_liters=blood_required_liters,
            days_in_hospital=days_in_hospital
        )

        # Check if the blood bank can fulfill the patient's needs
        if check_blood_bank_availability(patient):
            return JsonResponse({'success': True})
        else:
            patient.delete()  # Rollback patient creation
            return JsonResponse({'success': False, 'message': 'Blood bank cannot fulfill the request'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

@require_GET
def is_critical_mode_on(request):
    critical_mode = check_and_update_critical_mode()
    return JsonResponse({'critical_mode': critical_mode})

def check_and_update_critical_mode():
    total_liters_required = sum(
        patient.blood_required_liters for patient in Patient.objects.all()
    )
    total_liters_available = sum(
        blood_inventory.quantity_liters for blood_inventory in BloodInventory.objects.all()
    )

    critical_mode = total_liters_required > total_liters_available
    BloodInventory.objects.update(critical_mode=critical_mode)

    return critical_mode

def check_blood_bank_availability(patient):
    blood_group = patient.blood_group
    blood_required_liters = patient.blood_required_liters

    try:
        blood_inventory = BloodInventory.objects.get(blood_group=blood_group)

        # Check if the blood bank can fulfill the patient's needs
        return blood_inventory.quantity_liters >= blood_required_liters
    except BloodInventory.DoesNotExist:
        return False

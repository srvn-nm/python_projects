from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET, require_http_methods  # تغییر این خط

from .models import Bed, Patient


@csrf_exempt
@require_POST
def set_total_beds(request):
    total_beds = int(request.POST.get('total_beds', 0))
    try:
        Bed.objects.bulk_create([Bed() for _ in range(total_beds)])
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

@csrf_exempt
@require_POST
def admit_patient(request):
    patient_name = request.POST.get('patient_name', '')
    available_bed = Bed.objects.filter(occupied=False).first()

    if available_bed:
        available_bed.occupied = True
        available_bed.patient_name = patient_name
        available_bed.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})

@require_GET
def get_empty_beds(request):
    empty_beds = Bed.objects.filter(occupied=False).count()
    return JsonResponse({'empty_beds': empty_beds})

@csrf_exempt
@require_http_methods(["DELETE"])  # تغییر این خط
def discharge_patient(request):
    patient_name = request.POST.get('patient_name', '')
    try:
        bed = Bed.objects.get(patient_name=patient_name)
        bed.occupied = False
        bed.patient_name = None
        bed.save()
        return JsonResponse({'success': True})
    except Bed.DoesNotExist:
        return JsonResponse({'success': False})

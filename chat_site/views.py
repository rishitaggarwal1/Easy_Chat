from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def login(request):
    from random import randint
    otp = 0
    if request.method == "POST":
        phone_no = request.POST['phone_no']
        otp = randint(11111, 99999)
        print("Rishit")
        # return render(request, 'login.html', {
        #     'otp': otp
        # })
    return render(request, 'login.html', {})

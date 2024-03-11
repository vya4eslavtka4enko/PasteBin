from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def create_user(request):
    return render(request,'user_registration.html')


def user_enter(request):
    if request.method == "POST":
        print('hello')
    return render(request,'main.html')
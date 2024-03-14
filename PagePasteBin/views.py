from django.shortcuts import render,redirect
from .models import User
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')


def create_user(request):
    all_user = ''
    if request.method == "POST":
        user_email = request.POST.get('user_email')
        user_name = request.POST.get('user_name')
        user_password = request.POST.get('user_password')
        User.objects.create(user_name=user_name,email_name=user_email,user_password=user_password)
    return render(request,'user_registration.html', {'users':all_user})



def user_enter(request):
        print("hello")
    # if request.method == "POST":
        enter_user_email=request.POST.get('enter_user_email')
        enter_user_pass=request.POST.get('enter_user_pass')
        print(enter_user_pass)
        print(enter_user_email)
        # if not User.objects.filter(email_name = enter_user_email,user_password = enter_user_pass):
        #     print('no')
        # else:
        #     print("yes")
        #     return render(request,  'main.html')
        return render(request, 'index.html')




def add_post(request):
    return render(request,'add_post.html')



def create_new_post(request):
    element = {
        'element':"""  <div class="container">
        <div class="card">
        <div class="card-header">
        Quote
        </div>
        <div class="card-body">
        <button type="button" class="close" aria-label="Close">
        <span aria-hidden="true">&times;</span>
        </button>
        <blockquote class="blockquote mb-0">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
        <footer class="blockquote-footer">Someone famous in <cite title="Source Title">Source Title</cite></footer>
        </blockquote>
        </div>"""
    }
    return render(request,'main.html',element)
from django.shortcuts import render,redirect
from .models import User
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')


def create_user(request):
    all_user = ''
    if request.method == "POST":
        User.objects.create(user_name='',email_name='')




    # if request.method == 'POST':
    #     if form.is_valid():
    #         user=form.save(commit=False)
    #         user.user_name=request.user
    #         user.save()
    #         return redirect('/')
    #     else:
    #         # The supplied form contained errors - just print them to the terminal.
    #         print(form.errors)
    # else:
    #     # If the request was not a POST, display the form to enter details.
    #     form = User()
    #
    #     # Bad form (or form details), no form supplied...
    #     # Render the form with error messages (if any).
    return render(request,'user_registration.html', {'users':all_user})



def user_enter(request):
    # if request.method == "POST":
     return render(request,'main.html',)


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
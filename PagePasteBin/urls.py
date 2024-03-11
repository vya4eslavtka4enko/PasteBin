from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name = 'index'),
    path('registration',views.create_user,name = 'user_registration'),
    path('mainPage',views.user_enter,name = 'enter_user')
]
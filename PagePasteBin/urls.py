from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name = 'index'),
    path('registration',views.create_user,name = 'user_registration'),
    path('main_page',views.user_enter,name = 'user_enter'),
    path('add_post',views.add_post,name = "add_post"),
    path('create_new_post',views.create_new_post,name='create_new_post')
]
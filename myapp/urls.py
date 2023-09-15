from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('create/',views.create,name='create'),
    path('signup/',views.sign_up,name='signup'),
    path('login/',views.log_in,name='login')
]

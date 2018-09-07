from django.urls import include, path
from AppTwo import views

urlpatterns = [
    path('',views.index, name='index'),
    path('help/',views.help, name='help'),
    path('users/',views.users, name='users'),
    path('register/',views.register,name='register')
]

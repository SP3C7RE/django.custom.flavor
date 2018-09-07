from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
# from . import forms
from AppTwo.forms import UsersForm
# Create your views here.

def index(request):
    my_dict = {'insert_me': 'This is inserted from ProTWO!'}
    return render(request,'ProTwo/index.html',context=my_dict)

def users(request):
    allUsers = User.objects.all()
    myDict = {'allUsers': allUsers }
    return render(request,'ProTwo/user.html',context=myDict)

def help(request):
    return render(request,'ProTwo/help.html')

def register(request):

    form = UsersForm()

    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('INVALID SUBMIT')

    return render(request,'ProTwo/register.html',{'form':form})

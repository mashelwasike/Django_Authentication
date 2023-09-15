from django.shortcuts import render,redirect
from . models import Information
from . forms import InformationForms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'home.html')

def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request,'signup.html',{'form':form})

def log_in(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})

@login_required(login_url='login')
def create(request):
    if request.method == "POST":
        form = InformationForms(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author =  request.user
            instance.save()
            return redirect('home')
    else:       
        form = InformationForms()
    return render(request,'create.html',{'form':form})

def logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')


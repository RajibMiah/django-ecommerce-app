
from django.http import HttpResponse
from django.shortcuts import render
from .forms import AccountFrom
from django.contrib.auth import authenticate , logout , login

# Create your views here.

def register(request):
    
    if request.user.is_authenticated: 
        return HttpResponse('You have redirect to base url')

    form = AccountFrom()
    
    if request.method == 'post' or request.method == 'POST':
        form = AccountFrom(request.POST)
        print('form=========' , form)
        if form.is_valid():
            form.save()
            print("user name" ,form.cleaned_data['username'])
            return HttpResponse('account has been created')
            # REDIRECT TO E COMMERCE HOME PAGE OR PROFILE PAGE

    context = {'form': form}

    return render(request , 'register.html' , context)

def customerLogin(request):
    if request.user.is_authenticated:
        return HttpResponse('User is already logged in')
    else:
        if request.method == 'post' or request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
    
            customer = authenticate(request , username = username , password = password)

            if customer is not None:
                login(request , customer)
                return HttpResponse('You are logged in successfully!!')
            else:
                return HttpResponse("404")        

    return render(request , 'login.html' )
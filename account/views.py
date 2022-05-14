

import imp
from django.http import HttpResponse
from django.shortcuts import render
from .forms import AccountFrom
# Create your views here.

def register(request):
    
    if request.user.is_authenticated: 
        return HttpResponse('You have redirect to base url')

    form = AccountFrom()
    
    if request.method == 'post' or request.method == 'POST':
        form = AccountFrom(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('account has been created')
            # REDIRECT TO E COMMERCE HOME PAGE OR PROFILE PAGE
        else:
            form = AccountFrom()

    context = {'form': form}

    return render(request , 'register.html' , context)

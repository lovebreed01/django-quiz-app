from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        print(request.user.is_authenticated)
        return redirect('quizhome')
    elif request.method == 'POST':
        signupform = UserCreationForm(request.POST)
        if signupform.is_valid():
            signupform.save()
            return redirect('login')
    else:
        return render(request, 'landing/signup.html', context={
            'signupform':UserCreationForm()
        })
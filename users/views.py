from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts_list")
    else:
        messages.warning(request, message="Please make sure you fill the form in a valid way.")
        form = UserCreationForm()
    return render(request, 'users/register.html', {"form": form})

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():

            return redirect("posts_list")
    else:
        form = AuthenticationForm
    
    return render(request, 'users/login.html', {"form":form})
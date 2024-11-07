from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:list")
    else:
        messages.warning(request, message="Please make sure you fill the form in a valid way.")
        form = UserCreationForm()
    return render(request, 'register.html', {"form": form})

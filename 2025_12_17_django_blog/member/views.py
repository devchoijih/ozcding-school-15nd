from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login as django_login


# Create your views here.

def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog_list")
    else:
        form = UserCreationForm()

    context = {"form": form}
    return render(request, "registration/signup.html", context)

def login(request):
    form = AuthenticationForm(request, request.POST or None)
    if form.is_valid():
        django_login(request, form.get_user())

        next = request.GET.get("next")
        if next:
            return redirect(next)

        return redirect(reverse("blog_list"))

    return render(request, "registration/login.html")

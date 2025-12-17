from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


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

from django.shortcuts import render

# Create your views here.


def user_login(request):
    return render(request, "user_auth/user_login.html")


def user_signup(request):
    return render(request, "user_auth/user_signup.html")


def user_logout(request):
    return render(request, "user_auth/user_logout.html")


def password_reset(request):
    return render(request, "user_auth/password_reset.html")

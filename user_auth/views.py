from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# from django.views.decorators.http import require_POST
from django.contrib import messages

# Create your views here.


def user_login(request):
    return render(request, "user_auth/user_login.html")


def user_signup(request):
    if request.method == "POST":
        signup_name = request.POST["signup-name"]
        signup_email = request.POST["signup-email"]
        signup_password = request.POST["signup-password"]
        try:
            user_exists = User.objects.get(username=signup_name)
            print()
            messages.add_message(
                request, messages.INFO, f"Este usuário já exite: {user_exists}"
            )

        except User.DoesNotExist:
            new_user = User.objects.create_user(
                signup_name, signup_email, signup_password
            )
            new_user.save()
            return redirect("user_auth:user_login")

    return render(request, "user_auth/user_signup.html")


def user_logout(request):
    return render(request, "user_auth/user_logout.html")


def password_reset(request):
    return render(request, "user_auth/password_reset.html")

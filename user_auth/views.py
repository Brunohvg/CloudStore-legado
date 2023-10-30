from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# from django.views.decorators.http import require_POST
from django.contrib import messages

# Create your views here.


def user_login(request):
    if request.method == "POST":
        signin_email = request.POST["signin-email"]
        signin_password = request.POST["signin-password"]

        try:
            user_name = User.objects.get(email=signin_email)
            user_authenticate = authenticate(
                request, username=user_name, password=signin_password
            )
            if user_authenticate is not None:
                login(request, user=user_authenticate)
                print("ok")
                return redirect("user_auth:user_logout")
            else:
                messages.add_message(
                    request, messages.INFO, message="E-mail ou senha incorretos"
                )

        except User.DoesNotExist:
            messages.add_message(
                request,
                messages.INFO,
                message="Este e-mail, não existe",
            )

    return render(request, "user_auth/user_login.html")


def user_signup(request):
    if request.method == "POST":
        signup_name = request.POST["signup-name"]
        signup_email = request.POST["signup-email"]
        signup_password = request.POST["signup-password"]
        try:
            user_exists = User.objects.get(username=signup_name)

            messages.add_message(
                request,
                messages.INFO,
                f"O usuário, {user_exists} já exite no nosso sistema ",
            )

        except User.DoesNotExist:
            new_user = User.objects.create_user(
                signup_name, signup_email, signup_password
            )
            new_user.save()
            return redirect("user_auth:user_login")

    return render(request, "user_auth/user_signup.html")


def password_reset(request):
    return render(request, "user_auth/password_reset.html")


def user_logout(request):
    return render(request, "user_auth/user_logout.html")

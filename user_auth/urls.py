from django.urls import path
from . import views

app_name = "user_auth"

urlpatterns = [
    path("", views.user_login, name="user_login"),  # Rota Logar User
    path("signout/", views.user_signup, name="user_signup"),  # Rota Cadastrar User
    path("password_reset/", views.password_reset, name="password_reset"),
    # Rota Resetar Senha
    path("logout/", views.user_logout, name="user_logout"),  # Deslogar User
]

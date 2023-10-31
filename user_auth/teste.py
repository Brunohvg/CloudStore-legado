from django.core.mail import send_mail


send_mail(
    "Assunto",
    "Esse e o email que estou enviando",
    "quemestaenvidao@gmail.com",
    ["lojasbibelo@gmail.com"],
)

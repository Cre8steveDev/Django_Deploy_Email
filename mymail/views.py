from django.shortcuts import render, redirect

from django.core.mail import EmailMultiAlternatives  # send_mail,
from django.template.loader import render_to_string
import os


# Create your views here.
def index(request):
    if request.method == "POST":
        print(request.POST)
        sender_name = request.POST.get("name")
        sender_email = request.POST.get("email")
        sender_subject = request.POST.get("subject")
        sender_message = request.POST.get("message")

        server_mail = os.getenv("EMAIL_HOST_USER")

        html_content = render_to_string(
            "contact_mail.html",
            {
                "name": sender_name,
                "email": sender_email,
                "message": sender_message,
                "subject": sender_subject,
            },
        )

        msg = EmailMultiAlternatives(
            sender_subject, sender_message, server_mail, ["testing@gmail.com"]
        )

        msg.attach_alternative(html_content, "text/html")
        msg.send()

        # Call send mail function with values.BASIC
        # send_mail(
        #     sender_subject,
        #     sender_message
        #     + f"\n Sender Name: {sender_name} \n Sender Email: {sender_email}",
        #     server_mail,
        #     ["idemudiawisdom27@gmail.com"],
        # )

        return redirect("/")

    return render(request, "index.html")

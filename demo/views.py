from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMessage
# Create your views here.


def greet(request):
    subject = "Hi user"
    message = "this mail is sent from django"
    email_message = EmailMessage(subject, message,
                                 'uye@google.com', ['info@email.com'])
    email_message.attach_file('')
    email_message.send()
    return render(request, 'demo/hello.html')


def greet_me(request, name):
    return HttpResponse(f"let's xplore django {name}")

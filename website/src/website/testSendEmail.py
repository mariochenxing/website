from django.core.mail import send_mail
from django.http import HttpResponse

def sendEmail(request):
    send_mail('subject','this is the message of email','chen77452@126.com',['reseive@example.com'],fail_silently=True)
    return HttpResponse('successful')
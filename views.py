from django.shortcuts import render , redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def email(request):
    return render(request,'User/email.html')

def email_info(request):
    myto = request.POST['to']
    mysubject = request.POST['subject']
    mymesssage = request.POST['message']

    send_mail(mysubject,mymesssage,settings.EMAIL_HOST_USER, [myto] ,fail_silently=False)
    messages.success(request,'Email Send Successfully')
    return redirect('/User/email/')


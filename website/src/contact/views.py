from django.core.mail import send_mail
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from contact.forms import ContactForm
from django.template.context import RequestContext
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                #cd.get('email', 'chen77452@126.com'),
                'chen77452@126.com',
                ['1094089975@qq.com'],
                fail_silently=True
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render_to_response('contact_form.html',{'form':form},context_instance=RequestContext(request))
def thank(request):
    return render_to_response('thank.html')


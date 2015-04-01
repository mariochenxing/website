
from django.http import HttpResponse
from django.template import Template,Context
from django.template.loader import get_template
from django.core.context_processors import request
import datetime
from django.http import Http404
from django.shortcuts import render_to_response


def hello(request):
    return HttpResponse('Hello mario')
def homepage(request):
    return HttpResponse('hello')

def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html',{'current_date':now})

def hours_ahead(request,offset):
    #try:
    #    offset = int(offset)
    #except ValueError:
    #    raise Http404()
    dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
    html = "<html><body>IN %s hour(s),it will be %s.</body></html>"%(offset,dt)
    return HttpResponse(html)    
    
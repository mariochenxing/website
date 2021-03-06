
from django.http import HttpResponse
from django.template import Template,Context
from django.template.loader import get_template
from django.core.context_processors import request
import datetime
from django.http import Http404
from django.shortcuts import render_to_response
from urllib2 import Request
from symbol import except_clause
from books.models import Book
from django.template.defaultfilters import title
from website import sendemail


def hello(request):
    return HttpResponse('Hello mario')
def homepage(request):
    return HttpResponse('hello')

def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html',{'current_date':now})

def hours_ahead(request,hour_offset):
    try:
        hour_offset = int(hour_offset)
    except ValueError:
        raise Http404()
    next_time = datetime.datetime.now()+datetime.timedelta(hours=hour_offset)
    return render_to_response('hours_ahead.html',locals())

def ua_display_bad(request):
    ua = request.META['HTTP_USER_AGENT']
    return HttpResponse('your brower is %s'%ua)

def ua_display_good1(request):
    try:
        ua=request.META['HTTP_USER_AGENT']
    except KeyError:
        ua = 'unknown'
    return HttpResponse("your brower is %s"%ua)

def ua_display_good2(request):
    ua = request.META.get('HTTP_USER_AGENT','unknown')
    return HttpResponse("Your brower is %s"%ua)  
    
def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k,v in values:
        html.append(u'<tr><td>%s</td><td>%s</td></tr>'%(k,v))
    return HttpResponse('<table>%s</table>'%'\n'.join(html))


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q)>20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',
                {'books':books,'query':q})
    return render_to_response('search_form.html',
        {'errors':errors})
    
    

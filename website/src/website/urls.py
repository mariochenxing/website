from django.conf.urls import patterns, include, url
from django.contrib import admin
from website.views import hello, homepage, current_datetime, hours_ahead,\
    ua_display_good1, display_meta, search
from contact.views import contact, thank
from website import sendemail
from website.testSendEmail import sendEmail

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    ('^hello/$',hello),
    ('^$',homepage),
    ('^time/$',current_datetime),
    ('^timenow/$',current_datetime),
    (r'^time/plus/(\d{1,2})/$',hours_ahead),
    (r'^good1/$',ua_display_good1),
    (r'^meta/$',display_meta),
    (r'^search/$',search),
    (r'^contact/$',contact),
    (r'^mail/$',sendEmail),
    (r'^contact/thanks/$',thank),#...
)

from django.conf.urls import patterns, include, url
from django.contrib import admin
from website.views import hello, homepage, current_datetime, hours_ahead

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
    #...
)

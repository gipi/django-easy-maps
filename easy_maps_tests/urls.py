from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.shortcuts import render_to_response


admin.autodiscover()

def index(request):
    return render_to_response('index.html')


urlpatterns = patterns('',
    url(r'^$', direct_to_template, {
        'template': 'index.html',
        'extra_context': {
            'address': ["Ekaterinburg, Mira 33", "Ekaterinburg, Malysheva 45",],
        },
    }, 'index'),
    (r'^admin/', include(admin.site.urls)),
)

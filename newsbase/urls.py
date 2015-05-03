from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'newsapp.views.home', name='home'),

    url(r'^$', 'newsapp.views.home', name='home'),
    # url(r'^newsapp/', include('newsapp.foo.urls')),
    url('^category*', 'newsapp.views.category', name='category'),
    url('^add*', 'newsapp.views.add', name='add'),
)

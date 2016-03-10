from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('qa',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'question/(\d+)/', 'views.test'),
)

from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns = [
    url(r'reader_page/$', views.reader_page, name= 'reader_page'),
    url(r'entry_page$', views.entry_page, name = 'entry_page'),
]


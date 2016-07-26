from django.conf.urls import url
from django.contrib import admin
from . import views
from django.contrib import admin
from .models import Stock
from django import template
from django.template.loader import get_template
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

app_name = 'stock'

urlpatterns = [
    #http://localhost:8000/stock/  --> will trigger views.Index def(). in views.py
    url(r'^$', views.Index, name='Index'),
    # http://localhost:8000/stock/stockname/
    url(r'^stockname/', views.Stockname, name='Stockname'),
    # http://localhost:8000/stock/stockindicator/
    url(r'^stockindicator/', views.Stockindicator, name='Stockindicator'),]
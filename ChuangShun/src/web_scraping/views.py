from django.shortcuts import render, get_object_or_404
import requests
from nba_news.models import New

def home(request):
    qs = New.objects.all().order_by('-unique_id')
    context = {
        "objects_list" : qs
    }
    return render(request, "home.html", context)

def detail(request, id=None):
    instance = get_object_or_404( New , unique_id= id)
    context = {
        "list" : instance
    }
    return render(request, "detail.html", context)

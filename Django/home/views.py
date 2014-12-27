from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404


def home(req):
    return render(req,'home/index.html')

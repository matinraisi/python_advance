from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def Hello(request):
    p_list = Product.objects.all()
    return HttpResponse(p_list)
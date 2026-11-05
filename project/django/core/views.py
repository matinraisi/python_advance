from django.shortcuts import render
from .models import Product

def Hello(request):
    p_list = Product.objects.all()
    context = {
        'products': p_list

        }
    
    return render(request, 'core/index.html',context )
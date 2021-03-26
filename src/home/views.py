from django.http import HttpResponse
from django.shortcuts import render
from . models import product
from math import ceil

# Create your views here.
def index(request):
    return render(request,'home/index.html')

def productInfo(request):
    return HttpResponse("We are at product page")

def index(request):
    prods= product.objects.all()
    n= len(prods)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': prods}
    return render(request,"home/index.html", params)

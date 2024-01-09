from django.shortcuts import render
from django.http import HttpResponse
from .forms import productform

# Create your views here.
def indexproduct(request):
    proform=productform()
    return render(request,'product.html',{'f':proform})
def addproduct(request):
    try:
        if request.method=="POST":
            pform=productform(request.POST)
            print(pform)
            if pform.is_valid():
                pform.save()
        return render(request,'product.html',{'f':pform,'msg':'Product Added'})
    except Exception as e:
        print(e)
        return HttpResponse("Error")

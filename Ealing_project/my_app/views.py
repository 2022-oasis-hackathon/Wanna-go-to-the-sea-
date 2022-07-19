from django.shortcuts import render
from . import models

# Create your views here.
def mainpage(request):  
    if request.method == 'GET':
        products = models.house.objects.all()
        context = {
            'region1' : products[:5],
            'region2' : products[5:10],
            'recommendation1' : products[10:15],
            'recommendation2' : products[15:20]
        }

        return render(request, 'my_app/mainpage.html', context = context)
    
    #return render(request, 'my_app/mainpage.html')
    

def page1(request): 
    return render(request, 'my_app/page1.html')

def page2(request):
    return render(request, 'my_app/page2.html')

def page3(request):
    return render(request, 'my_app/page3.html')
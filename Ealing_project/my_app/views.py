from django.shortcuts import render
from models import Item

# Create your views here.
def mainpage(request):
    '''
    if request.method == 'GET':
        products = Item.objects.all()
        context = {'products' : products}    
        return render(request, 'my_app/mainpage.html', context)
    '''
    return render(request, 'my_app/mainpage.html')
    

def page1(request): 
    return render(request, 'my_app/page1.html')

def page2(request):
    return render(request, 'my_app/page2.html')

def page3(request):
    return render(request, 'my_app/page3.html')
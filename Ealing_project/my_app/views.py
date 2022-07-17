from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request, 'my_app/mainpage.html')

def page1(request): 
    return render(request, 'my_app/page1.html')

def page2(request):
    return render(request, 'my_app/page2.html')

def page3(request):
    return render(request, 'my_app/page3.html')
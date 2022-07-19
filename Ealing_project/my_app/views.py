from django.shortcuts import render
from . import models
from my_app.models import region_detail_page

# 홈
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
    

#체험
def experience(request):
    if request.method == 'GET':
        products = models.house.objects.all()
        context = {
            'recommendation1' : products[10:15],
            'recommendation2' : products[15:20]
        }
        return render(request, 'my_app/experience.html', context = context)


#스팟
def spotmap(request):
    if request.method == 'GET':
        place = models.recommend_place.objects.all()
        context = {'place' : place}
        return render(request, 'my_app/spotmap.html', context = context)



def detail(request, topic):
    if request.method == 'GET':
            detail = models.region_detail_page.objects.all()
            context = {'detail' : detail, 'topic' : topic}
            return render(request, 'my_app/detail.html',context = context )

from django.shortcuts import render
from . import models
from my_app.models import region_detail_page, login_data

logined = False
print(logined)

# 홈
def mainpage(request):
    global logined
    if request.method == 'GET':
        products = models.house.objects.all()
        context = {
            'region1' : products[:5],
            'region2' : products[5:10],
            'recommendation1' : products[10:15],
            'recommendation2' : products[15:20],
            'logined' : logined,
        }
        return render(request, 'my_app/mainpage.html', context = context)

        
    
    #return render(request, 'my_app/mainpage.html')
    
#홈
def home(request):
    global logined
    if request.method == 'GET':
        context = {
            'logined' : logined
        }
        return render(request, 'my_app/home.html', context = context)

#로그아웃 되면서 홈가기
def logout(request):
    global logined
    logined = False
    if request.method == 'GET':
        context = {
            'logined' : logined
        }
        return render(request, 'my_app/home.html', context = context)


#체험
def experience(request):
    global logined
    if request.method == 'GET':
        products = models.house.objects.all()
        context = {
            'recommendation1' : products[10:15],
            'recommendation2' : products[15:20],
            'logined' : logined,
        }
        return render(request, 'my_app/experience.html', context = context)


#스팟
def spotmap(request):
    global logined
    if request.method == 'GET':
        place = models.recommend_place.objects.all()
        context = {
            'place' : place,
            'logined' : logined,
        }
        return render(request, 'my_app/spotmap.html', context = context)



def detail(request, topic):
    global logined
    if request.method == 'GET':
            detail = models.region_detail_page.objects.all()
            context = {'detail' : detail, 'topic' : topic, 'logined' : logined,}
            return render(request, 'my_app/detail.html',context = context )


def ex_detail(request):
    if request.method == 'GET':
        return render(request, 'my_app/ex_detail.html')


# 로그인
def login(request):
    global logined
    if request.method == "POST":
        username = request.POST["id"]
        password = request.POST["pw"]
        id_check = models.login_data.objects.all()

        print(id_check[0].login_id)
        print(username)
        print(password)
        check = {'id_check' : id_check}

        if id_check[0].login_id == username and id_check[0].login_password == password:
            print('로그인성공!')
            logined = True
            products = models.house.objects.all()
            context = {
                'region1' : products[:5],
                'region2' : products[5:10],
                'recommendation1' : products[10:15],
                'recommendation2' : products[15:20],
                'nickname' : username,
                'logined' : logined,
            }
            return render(request, 'my_app/mainpage.html', context = context)
        else:
            return render(request, "my_app/login.html")

    else:
        return render(request, 'my_app/login.html')


    
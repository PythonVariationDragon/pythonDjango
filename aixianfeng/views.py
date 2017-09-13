from django.shortcuts import render,HttpResponse,redirect
from .models import Wheel,Nav,Mustbuy,Shop,MainShow,FoodTypes,Goods,User
from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth import logout
import os
import time
import random
# Create your views here.

#主页视图
def main(request):
    loopList = Wheel.objects.all()
    navList = Nav.objects.all()
    mustbuy = Mustbuy.objects.all()
    shopList = Shop.objects.all()
    shop1 = shopList[0]
    shop2 = shopList[1:3]
    shop3 = shopList[3:7]
    shop4 = shopList[7:11]
    mainList = MainShow.objects.all()
    context = {
        'title':'首页',
        'loopWheelList':loopList,
        'navList':navList,
        'nav2List':mustbuy,
        'shop1':shop1,
        'shop2':shop2,
        'shop3':shop3,
        'shop4':shop4,
        'mainList':mainList
    }
    return render(request,'aixianfeng/main.html',context=context)


def market(request,pageid,cid,sortid):

    # 左侧数据
    leftList = FoodTypes.objects.all()
    # 右侧数据
    if cid == '0':
        goodsList = Goods.objects.filter(categoryid=pageid)
    else:
        goodsList = Goods.objects.filter(categoryid=pageid, childcid=cid)

    # 排序goodsList
    if sortid == '0':
        pass
    elif sortid == '1':
        goodsList = goodsList.order_by("productnum")
    elif sortid == '2':
        goodsList = goodsList.order_by("price")
    elif sortid == '3':
        goodsList = goodsList.order_by("-price")

    # 子类名称
    fllist = []
    foodtype = FoodTypes.objects.get(typeid=pageid)
    allcname = foodtype.childtypenames
    # "全部分类:0#进口零食:103547#饼干糕点:103544#膨化食品:103543#坚果炒货:103542#肉干蜜饯:103546#糖果巧克力:103545"
    idnames = allcname.split("#")
    for str in idnames:
        arr = str.split(":")
        fllist.append({"code": arr[1], "title": arr[0]})

    titlelist = [{"title": "综合排序", "index": "0"},
                 {"title": "销量排序", "index": "1"},
                 {"title": "价格最低", "index": "2"},
                 {"title": "价格最高", "index": "3"},]
    context = {
        "title": "闪送超市",
        "leftList": leftList,
        "goodsList": goodsList,
        "titlelist": titlelist,
        "id": pageid,
        "fllist": fllist,
    }
    return render(request, 'aixianfeng/market.html',context=context)

def market2(request):
    #get获取信息
    pageid = request.GET.get('pageid')
    cid = request.GET.get('cid')
    sortid = request.GET.get('sortid')
    # 左侧数据
    leftList = FoodTypes.objects.all()
    # 右侧数据
    if cid == '0':
        goodsList = Goods.objects.filter(categoryid=pageid)
    else:
        goodsList = Goods.objects.filter(categoryid=pageid, childcid=cid)

    # 排序goodsList
    if sortid == '0':
        pass
    elif sortid == '1':
        goodsList = goodsList.order_by("productnum")
    elif sortid == '2':
        goodsList = goodsList.order_by("price")
    elif sortid == '3':
        goodsList = goodsList.order_by("-price")

    # 子类名称
    fllist = []
    foodtype = FoodTypes.objects.get(typeid=pageid)
    allcname = foodtype.childtypenames
    # "全部分类:0#进口零食:103547#饼干糕点:103544#膨化食品:103543#坚果炒货:103542#肉干蜜饯:103546#糖果巧克力:103545"
    idnames = allcname.split("#")
    for str in idnames:
        arr = str.split(":")
        fllist.append({"code": arr[1], "title": arr[0]})

    titlelist = [{"title": "综合排序", "index": "0",'cid':cid},
                 {"title": "销量排序", "index": "1",'cid':cid},
                 {"title": "价格最低", "index": "2",'cid':cid},
                 {"title": "价格最高", "index": "3",'cid':cid},]
    context = {
        "title": "闪送超市",
        "leftList": leftList,
        "goodsList": goodsList,
        "titlelist": titlelist,
        "id": pageid,
        "fllist": fllist,
    }
    return render(request, 'aixianfeng/market2.html',context=context)

def cart(request):
    return render(request,'aixianfeng/cart.html',{'title':'购物车'})
def mine(request):
    username = request.session.get('username','未登录')
    context = {
        'title':'我的',
        'username':username,
    }
    return render(request,'aixianfeng/mine.html',context=context)


def register(request):
    context={
        'title':'注册'
    }
    return render(request,'aixianfeng/register.html',context=context)
#保存用户信息
def saveuser(request):
    useraccunt = request.POST.get("userAccount")
    userPass = request.POST.get("userPass")
    userName = request.POST.get("userName")
    userPhone = request.POST.get("userPhone")
    userAdderss = request.POST.get("userAdderss")
    f = request.FILES["userImg"]
    fpath = os.path.join(settings.MDEIA_ROOT,useraccunt+".png")
    with open(fpath,'wb') as pic:
        for data in f.chunks():
            pic.write(data)
    token = time.time() + random.randint(1,100000)
    token = '%d'%token
    user = User.createuser(useraccunt,userPass,userName,userPhone,userAdderss,fpath,0,token)
    user.save()
    request.session['username'] = userName
    request.session['token'] = token

    return redirect('/mine/')
#验证ID是否可用
def checkuserid(request):
    userid = request.POST.get('checkid')
    try:
        user = User.objects.get(userAccount=userid)
    except User.DoesNotExist as e:
        return JsonResponse({'data':0,'status':'success'})

    return JsonResponse({'data':0,'status':'error'})

def quit(request):
    logout(request)
    return redirect('/mine/')

def login(request):
    context = {
        "title": "登陆"
    }
    return render(request,'aixianfeng/login.html',context=context)



#登陆密码检验
def checkuserlogin(request):
    userccunt = request.POST.get('userAccount')
    userpassword = request.POST.get('userPasswd')

    try:
        user = User.objects.get(userAccount=userccunt)
    except:
        # return render(request,'aixianfeng/login.html',{'pass':'没有账号'})
        return JsonResponse({'data':'0','status':'error'})
    if userpassword != user.userPasswd:
        # return render(request,'aixianfeng/login.html',{'pass':'密码错误'})
        return JsonResponse({'data': '0', 'status': 'error'})
    request.session['username'] = user.userName
    request.session['token'] = user.userToken
    return redirect('/mine/')
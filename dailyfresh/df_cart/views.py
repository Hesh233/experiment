from django.shortcuts import render
from .models import CartInfo
from df_user.islogin import islogin
from django.http.response import HttpResponse ,JsonResponse
from django.contrib.redirects.models import Redirect
from django.http.response import HttpResponse, HttpResponseRedirect
@islogin
def cart(request):
    uid = request.session.get('userid')
    carts = CartInfo.objects.filter(user_id = uid)
    print(carts)
    context = {'page_cart':1,
               'carts':carts,
               'title':"购物车",
               }
    return render(request, 'df_cart/cart.html', context)
def add(request):
    try:
        uid = request.session.get('userid')
    except:
        return HttpResponseRedirect('/user/login')
    gid = request.GET.get('a')
    gnum = request.GET.get('b')
#     gid = int(gid)
#     gnum = int(gnum)
    carts = CartInfo.objects.filter(user_id=uid,goods_id=gid)
    if  carts:
        #购物车已经有该商品
        print(carts,' addcount   ')
        cart =carts[0]
        cart.count+=int(gnum)
        cart.save()
    else:
        print(carts,' addt   ')
        cart =  CartInfo()
        cart.user_id = uid
        cart.goods_id = gid
        cart.count = int(gnum)
        try:
            cart.save()   
        except:
            result = CartInfo.objects.filter(user_id = uid).count()  
            return JsonResponse({"count":result}) 
        
    result = CartInfo.objects.filter(user_id = uid).count()
    return JsonResponse({"count":result})
def edit(request, gid, count):
    try:
        cart = CartInfo.objects.get(id=gid)
        cart.count = int(count)
        cart.save()
        data = {'ok': 0}
    except Exception as e:
        data = {'ok': 1}
    return JsonResponse(data)
def delete(request, cart_id):
    try:
        cart = CartInfo.objects.get(id=cart_id)
        cart.delete()
        data = {'ok': 0}
    except Exception as e:
        data = {'ok': 1}
    return JsonResponse(data)
def getnum(request):
    try:
        uid = request.session.get('userid')
    except:
        return JsonResponse({"num":0})
    num = CartInfo.objects.filter(user_id=uid).count()
    return JsonResponse({"num":num})
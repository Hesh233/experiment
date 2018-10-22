from django.shortcuts import render
from django.template.context_processors import request
from df_user.islogin import islogin
from df_user.models import UserInfo
from df_goods.models import *
from df_cart.models import CartInfo
from decimal import * 
@islogin
def order(request):
    tran=10.00
    tran=Decimal.from_float(tran)
    userid = request.session.get("userid")
    carts = CartInfo.objects.filter(user_id = userid)
    user = UserInfo.objects.get(id = userid)
    count = carts.count()
    uphone = user.uphone[:3]+'****'+user.uphone[7:]
    sum=0
    sums=0
    for i in carts:
        sum = i.count*i.goods.gprice
        sums += sum
    print(type(sums),type(tran),sums)
    st =tran + sums
    context={"title":"订单",
             'carts':carts,
             'user':user,
             'uphone':uphone,
             'sums':sums,
             'count':count,
             'st':st,}
    return render(request,'df_order/place_order.html',context)
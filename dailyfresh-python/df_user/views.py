from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect,JsonResponse
from hashlib import sha1
from df_user.models import UserInfo
from df_user.islogin import islogin
from df_cart.models import CartInfo
from decimal import * 
from df_goods.models import *

def index(request):
    pass
def register(request):
    context = {'title':'注册'}
    return render(request,'df_user/register.html',context)
def register_handle(request):
    post = request.POST
    uname = post.get("user_name")
    upwd = post.get("pwd")
    ucpwd = post.get("cpwd")
    uemail = post.get("email")
    print(uname,upwd,ucpwd,uemail)
    if upwd!=ucpwd:
        return HttpResponseRedirect('user/register')
    s1=sha1()
    s1.update(upwd.encode())
    passwd2 = s1.hexdigest()
    user = UserInfo()
    user.uname = uname
    user.upwd = passwd2
    user.uemail = uemail
    user.save()
    
    return HttpResponseRedirect('user/login')
def register_exist(request):
    get = request.GET
    uname = get.get("uname")
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})
def login(request):
    try:
        uname = request.COOKIES["uname"]
        context = {'title':'登录','uname':uname,'error_pwd':0, 'error_name':0}
        return render(request,'df_user/login.html',context)
    except:
        context = {'title':'登录','error_pwd':0, 'error_name':0}
        return render(request,'df_user/login.html',context)
def login_handle(request):
    post=request.POST
    jizhu = post.get("jizhu")
    usname = post.get("username")
    upwd = post.get("pwd")
    print(usname,upwd)
    s1=sha1()
    s1.update(upwd.encode())
    passwd2 = s1.hexdigest()
    info = UserInfo.objects.filter(uname=usname)
    if info.count()==0:
        context={'title':'登录','info':'用户名不存在','error_name':1, 'error_pwd':0,'page_name': 0,'error_login':0,}
        return render(request,'df_user/login.html',context)
    print(info[0].upwd)
    if passwd2!=info[0].upwd:
        context={'title':'登录','info':'密码错误','error_pwd':1, 'error_name':0,'page_name': 0,'error_login':0,'uname':usname,}
        return render(request,'df_user/login.html',context)
    context={'uname':usname}
    url = request.COOKIES.get('url', '/user/info')
    request.session['userid'] = info[0].id
    request.session['username'] = info[0].uname
    request.session['islogin']=1
    red = HttpResponseRedirect(url) 
    print(url)
    if jizhu:
        red.set_cookie('uname', usname)
    else:
        red.set_cookie('uname', '')
   # return render(request,'df_user/user_center_info.html',context)
    return red 
def quitlogin(request):
    del request.session['userid']
    del request.session['username']
    del request.session['islogin']
    #return render(request,'df_user/login.html')
    red = HttpResponseRedirect('/user/login')
    return red
@islogin
def info(request):
#     try:
#     if not request.session.get('islogin') :             ###############登录判断,可以改成装饰器写
#         context={'error_login':1,'error_name':0, 'error_pwd':0,}
# #         return render(request,'df_user/login.html',context)
#         red = HttpResponseRedirect('/user/login')
#         red.set_cookie('url', request.get_full_path())
#         return red
#     except:
#             context={'error_login':1,'error_name':0, 'error_pwd':0,}
#             return render(request,'df_user/login.html',context)
    user_email = UserInfo.objects.get(id = request.session['userid']).uemail
    user_address = UserInfo.objects.get(id = request.session['userid']).uaddress
    user_phone = UserInfo.objects.get(id = request.session['userid']).uphone
    # 从cookies中读取最近浏览的信息
    goods_ids = request.COOKIES.get('goods_ids')
    if goods_ids and goods_ids != '':
        goods_ids = goods_ids.split(',')
    else:
        goods_ids = []
    # 遍历goods_ids列表 根据id搜索出每个产品 并添加到产品列表中
    goods_list = []
    for id in goods_ids:
        if id != '':
            goods = GoodsInfo.objects.get(id=id)
            goods_list.append(goods) 
    print(goods_ids)   
    context = {'title': '用户中心', 
               'user_name' : request.session['username'],
               'user_email' : user_email,
               'user_address': user_address,
               'user_phone': user_phone,
               'info':1,'page_name': 1,
                'goods_list': goods_list,}
    return render(request, 'df_user/user_center_info.html',context)
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
    context={
             'carts':carts,
             'user':user,
             'uphone':uphone,
             'sums':sums,
             'count':count,
             'st':st,order:'1','page_name': 1,'error_pwd':0,'error_name':0,"title":"全部订单",}
#     context={'order':1,'page_name': 1,'error_pwd':0, 'error_name':0,"title":"全部订单",}
    return render(request,'df_user/user_center_order.html',context)
@islogin 
def site(request):
    user = UserInfo.objects.get(id = request.session['userid'])
    if request.method == 'POST':
        # 当用户提交信息的时候 获取post参数
        post = request.POST
        user.ushou = post.get('ushou')
        user.uaddress = post.get('uaddress')
        user.uyoubian = post.get('uyoubian')
        user.uphone = post.get('uphone')
        user.save()
    else:
        # 当用户直接访问 url df_user/site 的时候 不进行任何操作
        pass
    if user.uphone!='':
        uphone1 = user.uphone[:3]+'****'+user.uphone[7:]
    else:uphone1=''
    context = {'title': '用户中心',
               'ushou' : user.ushou,
               'uaddress': user.uaddress,
               'uphone': uphone1,
               'site': 1,
               'page_name': 1,}
    return render(request, 'df_user/user_center_site.html', context)  
def site_handle(request):
    post = request.POST
    #print(post)
    uname = post.get('uname')
    ushou = post.get('ushou')
    uemail = post.get('uemail')
    uphone = post.get('uphone')
    uaddress = post.get('uaddress')
    user = UserInfo.objects.get(id=request.session['userid'])
    user.ushou = ushou
    user.uemail = uemail
    user.uphone = uphone
    user.uaddress = uaddress
    user.save()
    uphone1 = uphone[:3]+'****'+uphone[7:]
    context={'site':1,'message':'提交成功','uaddress':uaddress,'uaname':uname,
             'ushou':ushou,'umail':uemail,'uphone':uphone1,
             'page_name': 1,}
    return render(request,'df_user/user_center_site.html',context)
    
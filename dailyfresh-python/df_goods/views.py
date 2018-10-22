from django.core.paginator import Paginator
from django.shortcuts import render
from df_goods.models import GoodsInfo,TypeInfo
from django.template.context_processors import request
from django.http.response import HttpResponse, HttpResponseRedirect,JsonResponse
from df_user.islogin import islogin
from django.db.models import Q
from df_cart.models import CartInfo
def index(request):
    newfruit = GoodsInfo.objects.filter(gtype_id=1).order_by('-id')[:3]
    hotfruit = GoodsInfo.objects.filter(gtype_id=1).order_by('-gclick')[:4]
    newfish = GoodsInfo.objects.filter(gtype_id=2).order_by('-id')[:3]
    hotfish = GoodsInfo.objects.filter(gtype_id=2).order_by('-gclick')[:4]
    newmeat = GoodsInfo.objects.filter(gtype_id=3).order_by('-id')[:3]
    hotmeat = GoodsInfo.objects.filter(gtype_id=3).order_by('-gclick')[:4]
    newegg = GoodsInfo.objects.filter(gtype_id=4).order_by('-id')[:3]
    hotegg = GoodsInfo.objects.filter(gtype_id=4).order_by('-gclick')[:4]
    newvegetable = GoodsInfo.objects.filter(gtype_id=5).order_by('-id')[:3]
    hotvegetable = GoodsInfo.objects.filter(gtype_id=5).order_by('-gclick')[:4]
    newfrozen = GoodsInfo.objects.filter(gtype_id=6).order_by('-id')[:3]
    hotfrozen = GoodsInfo.objects.filter(gtype_id=6).order_by('-gclick')[:4]
    context = {'title':'首页',
               'guest_cart':1,
               'newfruit':newfruit,
               'hotfruit':hotfruit,
               'newfish':newfish,
               'hotfish':hotfish,
               'newmeat':newmeat,
               'hotmeat':hotmeat,
               'newegg':newegg,
               'hotegg':hotegg,
               'newvegetable':newvegetable,
               'hotvegetable':hotvegetable,
               'newfrozen':newfrozen,
               'hotfrozen':hotfrozen,
               }
    ren = render(request, 'df_goods/index.html', context)
    ren.set_cookie('url', request.get_full_path()) 
    return ren

def goodlist(request, typeid, pageid, sort):
    panum = 15
    newgood = GoodsInfo.objects.all().order_by('-id')[:2]
    sortlist = ['id','gprice','-gclick']
    respon1 = GoodsInfo.objects.filter(gtype_id=int(typeid)).order_by(sortlist[int(sort)-1])[(int(pageid)-1)*panum:int(pageid)*panum]
   # print(respon1)
   # respon2 = GoodsInfo.objects.all().order_by(sortlist[int(sort)-1])[(int(pageid)-1)*panum:int(pageid)*panum]
    page1= GoodsInfo.objects.filter(gtype_id=int(typeid)).count()
    typename = TypeInfo.objects.get(id=int(typeid))
   # print(page1)
    if page1>panum:
        page1 = page1//panum+1
    else:page1 = page1//panum
    page = []
    for i in range(1,page1+1):
        page.append(i)
   # print(page1)
    pageid = int(pageid)
#     typelist = TypeInfo.objects.all()    
#     print(typelist)
#     paginator = Paginator(respon1,panum)
#     goodList = paginator.page(int(pageid))
    context = {"title":'商品列表',
               'guest_cart':1,
               'respon1':respon1,
               'newgood': newgood,
               'page':page,
               'pageid':pageid,
               'typeid':typeid,
               'sort':sort,
#               'respon2':respon2,
               'typename':typename,
               }
    #return render(request,'df_goods/list.html',context)
    ren = render(request,'df_goods/list.html',context)
    ren.set_cookie('url', request.get_full_path()) 
    return ren
def search(request,pageid, sort,searc ):
    panum = 15
    sortlist = ['id','gprice','-gclick']
    respon1 = GoodsInfo.objects.filter(gtitle__contains=searc).order_by(sortlist[int(sort)-1])[(int(pageid)-1)*panum:int(pageid)*panum]
    print(respon1)
    newgood = GoodsInfo.objects.all().order_by('-id')[:2]
    sortlist = ['id','gprice','-gclick']
    page1= GoodsInfo.objects.filter(gtitle__exact=searc).count()
   # print(page1)
    if page1>panum:
        page1 = page1//panum+1
    else:page1 = page1//panum
    page = []
    for i in range(1,page1+1):
        page.append(i)
   # print(page1)
    pageid = int(pageid)
    context={"title":'商品列表',
               'guest_cart':1,
               'respon1':respon1,
               'newgood': newgood,
               'page':page,
               'pageid':pageid,
               'typeid':'搜索',
               'sort':sort,
#               'respon2':respon2,
               'typename':'搜索',
               'searc':searc,}
    #return render(request,'df_goods/list.html',context)
    ren = render(request,'df_goods/list.html',context)
    ren.set_cookie('url', request.get_full_path()) 
    return ren
@islogin 


def detail(request, goodid):
    goods = GoodsInfo.objects.get(id=goodid)
    goodsid = goods.gtype_id
    goods.gclick = goods.gclick + 1
    goods.save()
    newgood = GoodsInfo.objects.all().order_by('-id')[:2]
    goodtype = TypeInfo.objects.get(id=goodsid)
    uid = request.session.get('userid')
    result = CartInfo.objects.filter(user_id = uid).count()
    context = {"title":'商品详情',
               'guest_cart':1,
               'goodtype':goodtype,
               'goods':goods,
               'newgood': newgood,
               'goodsid':goodsid,
               'isdetail':1,
               'count':result,}
    response = render(request, 'df_goods/detail.html', context)
    print(request.COOKIES.get('goods_ids'))
    # 读取请求的cookies
    goods_ids = request.COOKIES.get('goods_ids')
    # 判断cookies中的商品id序列是否为空
    if goods_ids and goods_ids != '':
        # 不为空 以逗号进行分割 把字符串转换成列表
        goods_ids = goods_ids.split(',')
        # 如果列表中已经有当前的id 则需要移除
        if goodid in goods_ids:
            goods_ids.remove(goodid)
        # 把当前的id放到列表的前面
        goods_ids.insert(0, goodid)
        # 如果超过5个 则值保留前5个
        if len(goods_ids) > 5:
            goods_ids = goods_ids[0:5]
    else:
        # 为空
        goods_ids = goodid
    
    # 把列表重新拼接成字符串 
    goods_ids = ','.join(goods_ids)
    print(goods_ids)
    # 把响应数据存储到cookies中
    response.set_cookie('goods_ids', goods_ids)
    response.set_cookie('url', request.get_full_path()) 
    return response             #要接收cookies一定要返回response

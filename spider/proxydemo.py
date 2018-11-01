#使用代理demo
import ssl
from urllib import request
from urllib import parse
import random
from bs4 import BeautifulSoup 
import requests
from idlelib.rpc import response_queue
from http.cookiejar import *
def gethandler():
    ua_list=["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
         "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
         "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)",
         "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)"
]
    user_agent = random.choice(ua_list)  
    return  {"User-Agent":user_agent}   
 
def main():
    headers = gethandler()
    url = "https://baidu.com"
    req = request.Request(url,headers = headers)
    context = ssl._create_unverified_context()
    
    
    
    #代理
    proxyswitch = True
    proxyaddr = '106.75.226.36'
    proxyport = '808'
    proxytype = 'HTTPS'
    proxyuser = ''
    proxypasswd = ''
    if proxyswitch and proxyuser=='':
       httpproxy_handler= request.ProxyHandler({proxytype:proxyaddr+":"+proxyport})
    elif proxyswitch and proxyuser!='':
       httpproxy_handler = request.ProxyHandler({"HTTP":proxyaddr + ':' + proxyport})
    else:httpproxy_handler = request.ProxyHandler({})
    
    
    
    #http_handler = request.HTTPSHandler(context = context,debuglevel = 1)
    opener = request.build_opener(httpproxy_handler)
    response = opener.open(url)
    html = response.read()
    html = html.decode('utf-8')
    print(html)
if __name__ == '__main__':
    main()

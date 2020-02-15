# -*- coding: utf8 -*-
import requests
import json
from urllib.parse import quote
import time
##设置自己的openid，cookie的最后一行就是openid
openid = "" 
###设置server酱的sckey    server酱官网：http://sc.ftqq.com
sckey = ""

def qd():
    session = requests.session()
    url = "http://wx.ah.189.cn/AhdxTjyl/qd.do"
    headers = {"Cookie":"openid=" + openid,"User-Agent":"MicroMessenger/7.0.10.1580(0x27000A56) Process/tools NetType/WIFI Language/zh_CN ABI/arm64"}
    result = session.get(url,headers=headers)
    ##通过json处理数据 变成dict
    data = json.loads(result.text)            
    if data["obj"] == "None":
        print("签到成功")
        ##发送签到信息到server酱
        requests.get('https://sc.ftqq.com/' + sckey + '.send?text=' + quote('安徽电信自动签到成功~'+time.strftime('%Y.%m.%d',time.localtime(time.time()))))
    elif data["obj"] == "您今天已经签到了！":
        print("您今天已经签到了！")
        ##发送签到信息到server酱
        requests.get('https://sc.ftqq.com/' + sckey + '.send?text=' + quote('您今天已经签到了！'+time.strftime('%Y.%m.%d',time.localtime(time.time()))))
    else:
        print("签到失败")
        ##发送签到信息到server酱
        requests.get('https://sc.ftqq.com/' + sckey + '.send?text=' + quote('安徽电信自动签到失败~QAQ'+time.strftime('%Y.%m.%d',time.localtime(time.time())))) 

 

def main_handler(event, context):
    return qd()



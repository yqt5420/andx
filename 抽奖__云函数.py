# -*- coding: utf8 -*-
import requests
import re
###填写openid 在cookiede 最后一行就是####
id = ""

 ### 建立一个会话，可以把同一用户的不同请求联系起来；直到会话结束都会自动处理cookies###
session = requests.session()
def get_info(openid):
    url = "http://ahds.10006.info/ahdxcj/index.do?code=091rotyT0ZawE12ogfxT09dsyT0rotyV&state=123"
    headers = {"Upgrade-Insecure-Requests": "1","Cookie":"openid=" + openid,"User-Agent":"Mozilla/5.0 (Linux; Android 9; MI 8 Build/PKQ1.180729.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045111 Mobile Safari/537.36 MMWEBID/8116 MicroMessenger/7.0.10.1580(0x27000A56) Process/tools NetType/WIFI Language/zh_CN ABI/arm64"}
 
    ###获取网页信息###
    result = session.get(url,headers=headers)
    html = result.text
    get_value = re.compile("<script>.*?openid.*?'(.*?)'.*?phone.*?'(.*?)'.*?latnid.*?'(.*?)'.*?sign.*?'(.*?)'.*?qd.*?'(.*?)'",re.S)       #这里只需要返回的第一个结果即可，故用search
    get_cjjh = re.compile("<span id=\"gxcj\">(.*?)<",re.S)
    data = get_value.search(html)
    cjjh = get_cjjh.findall(html)
    print("剩余抽奖次数",cjjh)
    openid,phone,latnid,sign,qd = data[1],data[2],data[3],data[4],data[5]
    return openid,phone,latnid,sign,qd      #传出对应值

def cj():
    openid,phone,latnid,sign,qd = get_info(id)
    url1 = "http://ahds.10006.info/ahdxcj/cjtimes.do"
    url = "http://ahds.10006.info/ahdxcj/cj.do"
    data = {"openid":openid,"phone":phone,"latnid":latnid,"sign":sign,"qd":qd}
    data1 = {"openid":openid,"phone":phone,"latnid":latnid}
    result1 = session.post(url1,data=data1)
    result = session.post(url,data=data)
    return result1.text,result.text,phone

def main_handler(event, context):
    return print(cj())







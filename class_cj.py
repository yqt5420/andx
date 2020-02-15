import requests
import re
import json

class Lucky():
    url = "http://wx.ah.189.cn/ahwx/usercenter.do?code=001LWwOv0LeNed1yGSOv0ltgOv0LWwOW&state=123"
    get_info_url = "http://ahds.10006.info/ahdxcj/indexcj.do?code=001LWwOv0LeNed1yGSOv0ltgOv0LWwOW&state=123"
    cjtime_url = "http://ahds.10006.info/ahdxcj/cjtimes.do"
    cj_url = "http://ahds.10006.info/ahdxcj/cj.do"
    User_Agent = "Mozilla/5.0 (Linux; Android 9; MI 8 Build/PKQ1.180729.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/045111 Mobile Safari/537.36 MMWEBID/8116 MicroMessenger/7.0.10.1580(0x27000A56) Process/tools NetType/WIFI Language/zh_CN ABI/arm64"
    session = requests.session()
    def __init__(self,openid,JSESSIONID):
        self.id = openid
        self.JSESSIONID = JSESSIONID
        # self.cjjh,self.openid,self.phone,self.latnid,self.sign,self.qd = self.get_info()
        # self.final_result, self.final_name = self.cj()

    def get_url(self):
        # headers = {"Upgrade-Insecure-Requests": "1","Cookie":"JSESSIONID=" + self.JSESSIONID +"; " + "OPENID=" + self.id,"User-Agent":self.__class__.User_Agent}
        headers = {"Upgrade-Insecure-Requests": "1","Cookie":"JSESSIONID=4BC759EE4FFA42F56BBBA2BFA70138BC.jvm8081; wxUserInfo=%7B%22city%22%3A%22%E6%B1%A0%E5%B7%9E%22%2C%22country%22%3A%22%E4%B8%AD%E5%9B%BD%22%2C%22headimgurl%22%3A%22http%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2FeiaU5DzsicHmXQMCL7hLiabqhmwWrGIvafgb1wNSlGrqRhs53icqQ4UAqHQhiap6dGKibJ4bj1iaVe9jv7HtZuaFX9cE2hN7uCfnic6q%2F132%22%2C%22nickname%22%3A%22%E6%B7%A1%E7%84%B6%28%EF%BD%A2%EF%BD%A5%CF%89%EF%BD%A5%29%EF%BD%A2%E5%98%BF%22%2C%22openid%22%3A%22o0AN1jjHX1WJmxw-abgxoTMQtgbM%22%2C%22province%22%3A%22%E5%AE%89%E5%BE%BD%22%2C%22sex%22%3A%221%22%2C%22unionid%22%3A%22oTSf11DwEHWjOrOBuwoJ_PzXQ0Y4%22%7D; OPENID=o0AN1jjHX1WJmxw-abgxoTMQtgbM","User-Agent":self.__class__.User_Agent}
        result = self.__class__.session.get(self.__class__.url,headers=headers)
        # get_url = re.compile()
        print(result.text)


    def get_info(self):
        headers = {"Upgrade-Insecure-Requests": "1","Cookie":"openid=" + self.id,"User-Agent":self.__class__.User_Agent}
        ###获取网页信息###
        result = self.__class__.session.get(self.__class__.get_info_url,headers=headers)
        html = result.text
        get_value = re.compile("<script>.*?openid.*?'(.*?)'.*?phone.*?'(.*?)'.*?latnid.*?'(.*?)'.*?sign.*?'(.*?)'.*?qd.*?'(.*?)'",re.S)       #这里只需要返回的第一个结果即可，故用search
        # get_cjjh = re.compile("<span id=\"gxcj\">(.*?)<",re.S)
        data = get_value.search(html)
        openid,phone,latnid,sign,qd = data[1],data[2],data[3],data[4],data[5]  
        return openid,phone,latnid,sign,qd

    def cj(self):
        openid,phone,latnid,sign,qd = self.get_info()
        data = {"openid":openid,"phone":phone,"latnid":latnid,"sign":sign,"qd":qd}
        data1 = {"openid":openid,"phone":phone,"latnid":latnid}
        result1 = self.__class__.session.post(self.__class__.cjtime_url,data=data1)
        result = self.__class__.session.post(self.__class__.cj_url,data=data)
        temp = json.loads(result1.text)
        temp1 = json.loads(result.text)
        # print(result1.text,result.text,self.phone)
        # print(temp["result"],temp1["name"])
        return temp["result"],temp1["name"]

    def send_message(self):
        print(self.cj())
        final_result, final_name = self.cj()
        print(final_name,final_result)
        if final_result > 0:
            print("小伙纸，中奖了哟" + "中了" + self.final_name)
        else:
            print("很遗憾，你今天的运气很不好，毛线都没抽到")

a = Lucky("o0AN1jjHX1WJmxw-abgxoTMQtgbM","4BC759EE4FFA42F56BBBA2BFA70138BC.jvm8081")
a.get_url()

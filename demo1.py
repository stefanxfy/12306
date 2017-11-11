import sys
import requests
import ssl
import time
sys.path.append('D:\Apython2017.10.28\12306')
import getCode
import user
#获取验证码url   https://kyfw.12306.cn/passport/captcha/captcha-image
#验证url post   https://kyfw.12306.cn/passport/captcha/captcha-check
#data
# answer:194,109
# login_site:E
# rand:sjrand

#登录 url  https://kyfw.12306.cn/passport/web/login

'''
username:dds
password:fdfsdvvvvvvvvvvv
appid:otn

'''
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'
}
session=requests.session()
session.verify=False
session.headers=headers
def checkcode(img):
    r1=session.get("https://kyfw.12306.cn/passport/captcha/captcha-image")
    print(r1.status_code)
    with open('code.png','wb') as f:
        f.write(r1.content)
    code=getCode.codes(img,287)
    print(code)
    data={
        'answer':code,
        'login_site':'E',
        'rand':'sjrand'
    }
    r2=session.post("https://kyfw.12306.cn/passport/captcha/captcha-check",data=data)
    print(r2.text)



def login (username,password):
    checkcode('code.png')
    data={
        'username':username,
        'password':password,
        'appid': 'otn'
    }
    r3=session.post("https://kyfw.12306.cn/passport/web/login",data=data)
    print(r3.text)




if __name__ =='__main__':
    t1 = time.time()
    login(user.username,user.password)
    t2=time.time()
    print(t2-t1)




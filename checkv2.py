#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import re
import time
import os
import json

your_name = os.environ["YOUR_NAME"]
your_pwd = os.environ["YOUR_PWD"]
wechat_key = os.environ["WECHAT_KEY"] #not must
token = os.environ["TOKEN"]#not must
chat_id = os.environ["CHAT_ID"]#not must
form_data = os.environ["FORM"] #key=xxxxx那一大长串放进secret

def bot_post(text):
    if wechat_key != "":
        url1 = 'https://sctapi.ftqq.com/' + wechat_key + '.send?title=check_ok' + '&desp='+text+time.strftime("%m-%d", time.localtime())
        re_result = requests.get(url1)
        print(re_result.text)
    if token != "":
        url2 = 'https://api.telegram.org/bot'+token+'/sendMessage?chat_id='+chat_id+'&text='+text+time.strftime("%m-%d", time.localtime())
        re_result = requests.get(url2)
        print(re_result.text)


def buaaLogin(user_name, password):
    print("统一认证登录")

    postUrl = "https://app.buaa.edu.cn/uc/wap/login/check"
    postData = {
        "username": user_name,
        "password": password,
    }
    responseRes = requests.post(postUrl, data=postData)
    print(responseRes.text)
    return responseRes


def fillForm(res):
    s = requests.session()
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://app.buaa.edu.cn/site/buaaStudentNcov/index',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': res.headers['set-cookie']
    }
    r = s.post('https://app.buaa.edu.cn/buaaxsncov/wap/default/save', data=form_data, headers=headers)
    return r

def auto_apply_go_out():
    import requests
    import datetime
    now = datetime.datetime.now() 
    diff = datetime.timedelta( days = 1 )


    date_today = now.strftime('%Y-%m-%d')
    date_tomorrow = (now + diff).strftime('%Y-%m-%d')
    date_after2 = (now + diff + diff).strftime('%Y-%m-%d')

    url = 'https://n.buaa.edu.cn/site/apps/launch'
    # header = {'Host': 'n.buaa.edu.cn', 'Connection': 'keep-alive', 'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"', 'Accept': 'application/json, text/plain, */*', 'Content-Type': 'application/x-www-form-urlencoded', 'X-Requested-With': 'XMLHttpRequest', 'sec-ch-ua-mobile': '?0', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49', 'sec-ch-ua-platform': '"Windows"', 'Origin': 'https://n.buaa.edu.cn', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://n.buaa.edu.cn/v2/matter/start?id=998', 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'Cookie': 'AMCV_8E929CC25A1FB2B30A495C97%40AdobeOrg=1687686476%7CMCIDTS%7C19174%7CMCMID%7C83610749914022089121977987425737306926%7CMCAID%7CNONE%7CMCOPTOUT-1656590901s%7CNONE%7CMCAAMLH-1657188501%7C11%7CMCAAMB-1657188501%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-19181%7CvVersion%7C3.0.0; utag_main=v_id:0181b4153fee0070d1311fe096e005085003e07d00bd0$_sn:1$_se:10$_ss:0$_st:1656585634520$ses_id:1656583700464%3Bexp-session$_pn:6%3Bexp-session$vapi_domain:buaa.edu.cn; _ga=GA1.1.256970436.1656583838; _ga_N9WZ2Y6SV8=GS1.1.1656583838.1.1.1656583861.0; insert_cookie=24270140; PHPSESSID=ST-270216-NoZBOHP0rqBEguENs1TnF6OIaO0e70cf0988907; yzs_vjuid=268904; yzs_vjvd=5281fc951125de88092b7c480e0cc55d; yzs_vt=173693854', 'x-proxy-origin': 'http://10.248.157.66:5001', 'Accept-Encoding': 'gzip, deflate', 'Content-Length': '4080'}
    # data = {'data': '{"app_id":"998","node_id":"","form_data":{"1428":{"User_4":"杨文哲","User_6":"SY2002220","User_8":"电子信息工程学院","User_12":"15652579587","File_135":[],"Alert_148":"","Alert_192":"","Alert_271":"","Input_143":"地铁","Input_186":"","Input_191":"","Input_244":"","Input_245":"","Input_246":"","Input_247":"","Input_248":"","Input_249":"","Input_250":"","Input_251":"","Input_252":"","Input_253":"","Radio_131":{"value":"2","name":"研究生 postgraduate"},"Radio_150":{"name":""},"Radio_157":{"value":"离校","name":"离校 leaving the campus"},"Radio_172":{"name":""},"Radio_218":{"value":"4","name":"大运村通行门"},"Radio_257":{},"Radio_258":{},"Radio_269":{},"Radio_270":{},"Region_14":{"area":{"label":"","value":""},"city":{"label":"海淀区","value":"110108"},"address":"北京市/海淀区","details":"","province":{"label":"北京市","value":"110000"}},"Region_259":{"area":{"label":"","value":""},"city":{"label":"","value":""},"address":"","details":"","province":{"label":"","value":""}},"Region_260":{"area":{"label":"","value":""},"city":{"label":"","value":""},"address":"","details":"","province":{"label":"","value":""}},"Region_261":{"area":{"label":"","value":""},"city":{"label":"","value":""},"address":"","details":"","province":{"label":"","value":""}},"Region_262":{"area":{"label":"","value":""},"city":{"label":"","value":""},"address":"","details":"","province":{"label":"","value":""}},"Ximage_211":["https://n.buaa.edu.cn/site/attach/auth-download?file_id=963298"],"Calendar_210":"' + date_today + 'T16:00:00.000Z","Calendar_254":"","Calendar_255":"","Calendar_256":"","SelectV2_141":[{"name":"临时出入校：外出就医（不得离京，不前往中高风险地区）","value":"2","default":0,"imgdata":""}],"SelectV2_177":[],"SelectV2_180":[],"SelectV2_184":[],"SelectV2_243":[],"SelectV2_266":[],"ShowHide_144":"","ShowHide_263":"","Validate_103":"","Validate_105":"","Validate_176":"","Validate_215":"","Validate_272":"","MultiInput_45":"1","RepeatTable_145":[{"Calendar_47":"' + date_tomorrow +'T16:00:00.000Z","Calendar_50":"' + date_after2 +'T15:00:00.000Z"}]}},"userview":1}', 'step': '0', 'agent_uid': '', 'starter_depart_id': '246486'}

    header = {
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Microsoft Edge";v="104"',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://n.buaa.edu.cn/v2/matter/start?id=1246',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'data': '{"app_id":"1246","node_id":"","form_data":{"1594":{"User_4":"杨文哲","User_6":"SY2002220","User_8":"电子信息工程学院","User_12":"15652579587","Alert_148":"","Alert_192":"","Alert_219":"","Alert_271":"","Input_286":"","Input_301":"","Input_303":"","Input_305":"","Input_316":"","Input_317":"","Input_318":"","Input_329":"","Input_350":"","Input_351":"","Input_352":"","Input_379":"在校","Input_436":"","Radio_353":{},"Radio_354":{},"Radio_360":{"value":"2","name":"研究生"},"Radio_368":{},"Radio_411":{},"Radio_412":{},"Radio_418":{"value":"2","name":"大运村通行门"},"Region_14":{"area":{"label":"","value":""},"city":{"label":"","value":""},"address":"","details":"","province":{"label":"","value":""}},"Region_284":{"area":{"label":"","value":""},"city":{"label":"海淀区","value":"110108"},"address":"北京市/海淀区","details":"","province":{"label":"北京市","value":"110000"}},"Region_347":{"area":{"label":"","value":""},"city":{"label":"","value":""},"address":"","details":"","province":{"label":"","value":""}},"Select_302":{},"Ximage_405":["https://n.buaa.edu.cn/site/attach/auth-download?file_id=1195658"],"Ximage_421":[],"Calendar_335":null,"Calendar_336":null,"Calendar_337":null,"Calendar_407":"' + date_after2 + 'T16:00:00.000Z","Calendar_433":null,"SelectV2_289":[],"SelectV2_320":[],"SelectV2_324":[{"name":"临时出入校","value":2}],"SelectV2_326":[{"name":"就医","value":"就医"}],"SelectV2_358":[{"name":"副书记","value":"3","default":1,"imgdata":""}],"SelectV2_434":[],"SelectV2_435":[],"ShowHide_361":"","ShowHide_362":"","ShowHide_369":"","ShowHide_370":"","ShowHide_383":"","ShowHide_422":"","ShowHide_437":"","Validate_103":"","Validate_105":"","Validate_170":"","Validate_175":"","Validate_176":"","Validate_272":"","DataSource_367":"","DataSource_380":"","DataSource_425":"","MultiInput_334":"1","RepeatTable_145":[{"Calendar_47":"' + date_tomorrow + 'T23:00:00.000Z","Calendar_50":"' + date_today + 'T15:00:00.000Z"}]}},"userview":1}',
        'step': '0',
        'agent_uid': '',
        'starter_depart_id': '246486',
    }

    res = requests.request(method = 'POST', url = url, headers = header, data = data, verify = False)
    res_data = res.content.decode('utf8')
    print(res_data)

def main():
    result = fillForm(buaaLogin(your_name, your_pwd))
    print(result.text)
    bot_post(result.text)
    auto_apply_go_out()
    return("DONE")
main()

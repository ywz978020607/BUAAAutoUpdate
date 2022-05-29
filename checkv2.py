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
form_data = {
    'sfzs': '1',
    'bzxyy': '',
    'bzxyy_other': '',
    'brsfzc': '1',
    'tw': '',
    'sfcxzz': '',
    'zdjg': '',
    'zdjg_other': '',
    'sfgl': '',
    'gldd': '',
    'gldd_other': '',
    'glyy': '',
    'glyy_other': '',
    'gl_start': '',
    'gl_end': '',
    'sfmqjc': '',
    'sfzc_14': '1',
    'sfqw_14': '0',
    'sfqw_14_remark': '',
    'sfzgfx': '0',
    'sfzgfx_remark': '',
    'sfjc_14': '0',
    'sfjc_14_remark': '',
    'sfjcqz_14': '0',
    'sfjcqz_14_remark': '',
    'sfgtjz_14': '0',
    'sfgtjz_14_remark': '',
    'szsqqz': '0',
    'sfyqk': '',
    'szdd': '1',
    'area': '北京市 海淀区',
    'city': '北京市',
    'province': '北京市',
    'address': '北京市海淀区花园路街道老麻抄手(知春路店)北京航空航天大学大运村学生公寓',
    'geo_api_info': '{"type":"complete","position":{"Q":39.977510579428,"R":116.34294786241401,"lng":116.342948,"lat":39.977511},"location_type":"html5","message":"Get ipLocation failed.Get geolocation success.Convert Success.Get address success.","accuracy":90,"isConverted":true,"status":1,"addressComponent":{"citycode":"010","adcode":"110108","businessAreas":[{"name":"大钟寺村","id":"110108","location":{"Q":39.965569,"R":116.339877,"lng":116.339877,"lat":39.965569}},{"name":"五道口","id":"110108","location":{"Q":39.99118,"R":116.34157800000003,"lng":116.341578,"lat":39.99118}},{"name":"双榆树","id":"110108","location":{"Q":39.971882,"R":116.32657599999999,"lng":116.326576,"lat":39.971882}}],"neighborhoodType":"","neighborhood":"","building":"","buildingType":"","street":"知春路","streetNumber":"29号院","country":"中国","province":"北京市","city":"","district":"海淀区","towncode":"110108018000","township":"花园路街道"},"formattedAddress":"北京市海淀区花园路街道老麻抄手(知春路店)北京航空航天大学大运村学生公寓","roads":[],"crosses":[],"pois":[],"info":"SUCCESS"}',
    'gwdz': '',
    'is_move': '0',
    'move_reason': '',
    'move_remark': '',
    'realname': '杨文哲',
    'number': your_name,
    'uid': '401394',
    'created': '1653737805',
    'date': '20220528',
    'id': '13260932',
    'gwszdd': '',
}

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


def main():
    result = fillForm(buaaLogin(your_name, your_pwd))
    print(result.text)
    bot_post(result.text)
    return("DONE")
main()

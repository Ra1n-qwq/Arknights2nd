# -*- encoding: utf-8 -*-
'''
@File    :   arknightdaily.py
@Time    :   2021/04/28
@Author  :   Ra1n 
@Version :   1.0
'''
# here put the import lib
import json
import logging
import requests
import time
logging.basicConfig(
  level = logging.INFO,
  format = '%(asctime)s %(levelname)s %(message)s',
  datefmt = '%Y-%m-%dT%H:%M:%S')
def  Result(result, data):
  return json.dumps(
    {
      'result': result,
      'message': data
    },ensure_ascii=False
  )
def start(Dic):
  header={
    'Host': 'ak.hypergryph.com',
    'Connection': 'close',
    'Content-Length': '12',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'accept': 'application/json',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8',
    'Origin': 'https://ak.hypergryph.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://ak.hypergryph.com/activity/preparation',
    'Accept-Language': 'zh-CN,zh;q=0.9',
  }
  url='https://ak.hypergryph.com/activity/preparation/activity/share'
  url2='https://ak.hypergryph.com/activity/preparation/activity/roll'
  Payload='{"method":1}'
  Payload2="{}"  
  session=requests.session()
  for i in Dic:
    session.cookies.set('Cookie',i)
    r=session.post(url,headers=header,data=Payload)
    r2=session.post(url2,headers=header,data=Payload2)
    rdic=json.loads(r.text)
    rdic2=json.loads(r2.text)
    try:
      code=rdic['data']['todayFirst']
    except KeyError:
      code=rdic['statusCode']
    try:
      code2=rdic2['code']
    except KeyError:
      code2=rdic2['statusCode']
    if code ==True:
        logging.info ("分享成功！")
    elif code ==False:
        logging.info ("今天已经分享过了")
    else:
      err_result=Result("Error!",rdic)
      logging.info(err_result)
    while code2 ==0:
      r2=session.post(url2,headers=header,data=Payload)
      rdic2=json.loads(r2.text)
    else:
      if code2==400:
        result=Result("Success!",rdic2['message'])
        logging.info(result)
      else:
        result=Result("Error!",rdic2)
        logging.info(result)
    time.sleep(5)
if __name__ == "__main__":
  #只有一个账号时
  #   Dic=['你的账号的cookie']
  #有多个账号
  Dic=['你的第一个账号的cookie'
  ,'你的第二个账号的cookie'
  
  ]
  start(Dic)
  while True:   #每天4点执行一次
    now_localtime = time.strftime("%H:%M", time.localtime())
    if now_localtime == "04:00":
        start(Dic)
        time.sleep(61)
    else:
        time.sleep(29)
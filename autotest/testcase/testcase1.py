# coding = utf-8
import requests, time, sys, re
import urllib


def reaRes(res, res_check):
    res = res.decode().replace('":"',"=").replace('":',"=")
    res_check = res_check.split(';')
    for s in res_check:
        if s in res:
            pass
        else:
            return 'wrong' + s
    return 'pass'


if __name__ == '__main__':
    url = 'http://' + '127.0.0.1:8000' + '/login'
    headers = {'Authorization':'', 'Content-Type':'application/json'}
    data = None
    req = urllib.request.Request(url=url,data=data,headers=headers,method="GET")
    print('reqeust'+url)
    try:
        results = urllib.request.urlopen(req).read()
        print('reponse is get')
        print(results)
    except Exception as e:
        print('error')
    res = reaRes(results,'login')
    print(res)
    print('Done!')
    
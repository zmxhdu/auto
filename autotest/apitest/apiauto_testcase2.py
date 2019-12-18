import requests, time, re
import urllib
import pymysql
import json


HOSTNAME = '127.0.0.1'


def test_readSQLcase():
    sql = 'select id,apiname,apiurl,apimethod,apiparamvalue,apiresult,apistatus from apitest_apis'
    conn = pymysql.connect(user='root', passwd='zmxhdu', db='autotest', port=3306, host=HOSTNAME, charset='utf8')
    cursor = conn.cursor()
    aa = cursor.execute(sql)
    info = cursor.fetchmany(aa)
    print(info)
    for ii in info:
        case_list = []
        case_list.append(ii)
        interfaceTest(case_list)

    conn.commit()
    cursor.close()
    conn.close()


def interfaceTest(case_list):
    res_flags = []
    request_urls= []
    responses = []
    strinfo = re.compile('(seturl')
    for case in case_list:
        try:
            case_id = case[0]
            interface_name = case[1]
            method = case[2]
            url = case[3]
            param = case[4]
            res_check = case[5]
        except Exception as e:
            return '测试用例格式不正确！%s' %e

    if param == '':
        new_url = 'http://' + 'api.test.com.cm' + url
    elif param == 'null':
        url = strinfo.sub(str(seturl('seturl')), url)
        new_url = 'http://' + url
    else:
        url = strinfo.sub(str(seturl('seturl')), url)
        new_url = 'http://' + '127.0.0.1' + url
        request_urls.append(new_url)
    


if __name__ == '__main__':
    test_readSQLcase()
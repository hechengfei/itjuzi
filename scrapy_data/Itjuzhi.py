import requests
import urllib.request
import json
import re
import random
import string
import time
from combase import ComBase
userName = 'chen193713@126.com'
passWord = 'h389513'
headers0 = {
         "Accept": "application/json, text/plain, */*",
         "Connection": "keep-alive",
         "Authorization": "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3d3dy5pdGp1emkuY29tL2FwaS9hdXRob3JpemF0aW9ucyIsImlhdCI6MTU0NDE2OTE0MSwiZXhwIjoxNTQ0MjU1NTQxLCJuYmYiOjE1NDQxNjkxNDEsImp0aSI6IjNLQ05KWkRNQ2hRbWNndVEiLCJzdWIiOjY3NjM3NCwicHJ2IjoiMjNiZDVjODk0OWY2MDBhZGIzOWU3MDFjNDAwODcyZGI3YTU5NzZmNyJ9.0GDkPzEmfVjDKBOzJ-wNqOVK9PUg_SqTOAUyKyw7R3g",
         #"Referer": "https://www.itjuzi.com/company/2031",
         "Accept-Encoding": "gzip, deflate, br",
         "Accept-Language": "zh-CN,zh;q=0.9",
         "Host": "www.itjuzi.com",
         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
         "Cookie": "acw_tc=76b20f6215441653423292949e2f9e58f4632a5873ffc4e86045fb6870bd7a; gr_user_id=fd4ef7f3-d3fd-4d22-945d-394dd7d6624b; _ga=GA1.2.887876691.1544165357; _gid=GA1.2.240834218.1544165357; gr_session_id_eee5a46c52000d401f969f4535bdaa78=864579e2-ae69-434c-bfa6-1c6db36451a8; gr_session_id_eee5a46c52000d401f969f4535bdaa78_864579e2-ae69-434c-bfa6-1c6db36451a8=true; flag=676374-chen193713@sina.com-; _gat_gtag_UA_59006131_1=1"
        }

def getHeaders():
    url = "https://www.itjuzi.com/api/authorizations"
    cookie = ''.join(random.sample(string.ascii_letters + string.digits, 62))

    payload = "{\"account\":\"%s\",\"password\":\"%s\"}" % (userName, passWord)
    headers = {
        'Host': "www.itjuzi.com",
        'Connection': "keep-alive",
        'Content-Length': "51",
        'Accept': "application/json, text/plain, */*",
        'Origin': "https://www.itjuzi.com",
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
        'Content-Type': "application/json;charset=UTF-8",
        'Referer': "https://www.itjuzi.com/login?url=%2Fcompany",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Cookie': "acw_tc=%s" % cookie
    }

    response = requests.request("POST", url, data=payload, headers=headers).text
    response = json.loads(response)

    token = response['data']['token']
    headers = {
        'Accept': "application/json, text/plain, */*",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        'Authorization': "%s" % token,
        'Connection': "keep-alive",
        'Content-Length': "146",
        'Content-Type': "application/json;charset=UTF-8",
        'Cookie': "acw_tc=%s;" % cookie,
        'Host': "www.itjuzi.com",
        'Origin': "https://www.itjuzi.com",
        #'Referer': "https://www.itjuzi.com/company",
        'User-Agent': "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.33 Safari/534.3 SE 2.X MetaSr 1.0"
    }

    return headers






def get_detail_id(f):
        for line in f.readlines():
            s = line.rstrip('\n')
        return s


def get_detail_info(id,headers):
        info ={}
        products_info = []
        # com_quancheng = ''
        # com_faren = ''
        # com_zhuceziben = ''
        # com_chenglishjian = ''
        # com_gongsileixing = ''
        # com_dizhi = ''
        # com_gongsimingcheng = ''
        # com_gongsimingcheng2 = ''
        # com_rongzilunci = ''
        # com_zhucemingcheng = ''
        # com_guanwang = ''
        # com_webwangzhi = ''
        # com_weixin = ''
        # com_chengliyu = ''
        # com_state = ''
        # com_guimo = ''

        time.sleep(1 + random.random() * 3)
        ua_list = [
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 ',
            '(KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
            'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
            'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
            'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)',
        ]
        # proxies = {'http': 'http://220.249.176.252:8118'}
        # 处理请求头
        headers['Referer'] = "https://www.itjuzi.com/company/"+id
        headers['User-Agent'] =random.choices(ua_list)
        url = "https://www.itjuzi.com/api/companies/"+id +"?type=person"
        url1 = "https://www.itjuzi.com/api/companies/" + id + "?type=icp"
        url2 = "https://www.itjuzi.com/api/companies/" + id + "?type=basic"
        try:
                response = requests.get(url,headers)
                print(response.text)
                response1 = requests.get(url1, headers)
                print(response1.text)
                response2 = requests.get(url2, headers)
                print(response2.text)
                #獲取產品信息
        except (TimeoutError,ConnectionError,ConnectionError) as e:
                print('遇到了反爬虫1，休息10秒')
                time.sleep(10 + random.random() * 5)
                headers = getHeaders()
                get_detail_info(id, headers)





        # if status != 'success':
        #     print('遇到了反爬虫1，休息10秒')
        #     time.sleep(10 + random.random() * 5)
        #     headers = getHeaders()
        #     get_detail_info(id, headers)
        ss = json.loads(response.text)['data']['products']
        if ss:

            for s in ss:
                 name = s['name']
                # print(name)
                 products_info.append(name)
        info.update({'products_info':products_info})
        #json.dumps()



        if json.loads(response1.text)['data']['elecredit']:
            com_quancheng = json.loads(response1.text)['data']['elecredit']['elecredit_basic']['entname']
            info.update({'com_quancheng':com_quancheng})
            com_faren = json.loads(response1.text)['data']['elecredit']['elecredit_basic']['frname']
            info.update({'com_faren': com_faren})
            com_zhuceziben =json.loads(response1.text)['data']['elecredit']['elecredit_basic']['regcap']
            info.update({'com_zhuceziben': com_zhuceziben})
            com_chenglishjian = json.loads(response1.text)['data']['elecredit']['elecredit_basic']['esdate']
            info.update({'com_chenglishjian': com_chenglishjian})
            com_gongsileixing = json.loads(response1.text)['data']['elecredit']['elecredit_basic']['enttype']
            info.update({'com_gongsileixing': com_gongsileixing})
            com_dizhi = json.loads(response1.text)['data']['elecredit']['elecredit_basic']['dom']
            info.update({'com_dizhi': com_dizhi})



        if json.loads(response2.text)['data']['basic']:
            com_gongsimingcheng = json.loads(response2.text)['data']['basic']['com_name']
            info.update({'com_gongsimingcheng': com_gongsimingcheng})
            com_gongsimingcheng2 = json.loads(response2.text)['data']['basic']['com_sec_name']
            info.update({'com_gongsimingcheng2': com_gongsimingcheng2})
            com_rongzilunci = json.loads(response2.text)['data']['basic']['com_round_name']
            info.update({'com_rongzilunci': com_rongzilunci})
            com_zhucemingcheng = json.loads(response2.text)['data']['basic']['com_registered_name']
            info.update({'com_zhucemingcheng': com_zhucemingcheng})
            com_guanwang = json.loads(response2.text)['data']['basic']['com_url']
            info.update({'com_guanwang': com_guanwang})
            com_webwangzhi = json.loads(response2.text)['data']['basic']['com_weibo_url']
            info.update({'com_webwangzhi': com_webwangzhi})
            com_weixin = json.loads(response2.text)['data']['basic']['com_weixin_url']
            info.update({'com_weixin': com_weixin})
            com_chengliyu = json.loads(response2.text)['data']['basic']['com_born_date']
            info.update({'com_chengliyu': com_chengliyu})
            com_state = json.loads(response2.text)['data']['basic']['com_status_name']
            info.update({'com_state': com_state})
            if json.loads(response2.text)['data']['basic']['company_scale']:
                com_guimo = json.loads(response2.text)['data']['basic']['company_scale']['com_scale_name']
                info.update({'com_guimo': com_guimo})
            else:
                com_guimo = ''
        return  info


if __name__ == '__main__':

    with open('E:\itjuzi\scrapy_data\id.txt') as fo:
         i = 0
         for line in fo.readlines():
             i = i + 1
             id = line.rstrip('\n')
             print(str(i)+',id:为' +id)
             try:
                 com = get_detail_info(id,headers0)
                 with open('E:\\工作相关\\工作任务\爬虫数据\\result.txt', 'a',encoding='utf-8')as fs:
                     fs.write('\n')
                     json.dump(com, fs, ensure_ascii=False)
                     print('第' + str(i) + '行执行完毕')
             except KeyError as e:
                 print('第' + str(i) + '行执行失败id为:'+id)
                 with open('E:\\itjuzi\\scrapy_data\\exception','w') as f:
                        f.write(id + '\n')
                 pass
                 print(e)


    # print(com.products_info)
    # print(com.com_quancheng)
    # print(com.com_faren)
    # print(com.com_zhuceziben)
    # print(com.com_chenglishjian)
    # print(com.com_gongsileixing)
    # print(com.com_dizhi)
    # print(com.com_gongsimingcheng)
    # print(com.com_gongsimingcheng2)
    # print(com.com_rongzilunci)
    # print(com.com_zhucemingcheng)
    # print(com.com_guanwang)
    # print(com.com_webwangzhi)
    # print(com.com_weixin)
    # print(com.com_chengliyu)
    # print(com.com_state)
    # print(com.com_guimo)




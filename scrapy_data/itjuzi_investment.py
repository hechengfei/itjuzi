import requests
import json
import re
import string
import random
import time
userName = '1937131977@qq.com'
passWord = 'h389513'
headers0 = {

"Accept": "application/json, text/plain, */*",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-CN,zh;q=0.9",
"Authorization": "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3d3dy5pdGp1emkuY29tL2FwaS9hdXRob3JpemF0aW9ucyIsImlhdCI6MTU0NDA2MTE0MywiZXhwIjoxNTQ0MTQ3NTQzLCJuYmYiOjE1NDQwNjExNDMsImp0aSI6IlJZVDZnemdvR2Z2akI1RTAiLCJzdWIiOjY3NTc4NywicHJ2IjoiMjNiZDVjODk0OWY2MDBhZGIzOWU3MDFjNDAwODcyZGI3YTU5NzZmNyJ9.7gcJ5ihEYqmth0bcd6UpuwiAW5dlnNfPanYaP1FQxgQ",
"Connection": "keep-alive",
"Content-Type": "application/json;charset=UTF-8",
"Cookie": "acw_tc=781bad2215440592701237042e0839474a8498b48f0c7a60d93b382069c286; gr_user_id=7c398330-8d13-48c6-92d1-35ca90849d4d; _ga=GA1.2.2064967636.1544059296; _gid=GA1.2.881417616.1544059296; gr_session_id_eee5a46c52000d401f969f4535bdaa78=1fcf4c27-3f01-40ec-95d9-5e741598d84f; flag=675787-1937131977@qq.com-; gr_session_id_eee5a46c52000d401f969f4535bdaa78_1fcf4c27-3f01-40ec-95d9-5e741598d84f=true; _gat_gtag_UA_59006131_1=1",
"Host": "www.itjuzi.com",
"Origin": "https://www.itjuzi.com",
"Referer": "https://www.itjuzi.com/investfirm",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
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
        'Referer': "https://www.itjuzi.com/investfirm",
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
    }

    return headers


headers0 = getHeaders()


url = "https://www.itjuzi.com/api/investments"


def  get_invest_info(pageNum,headers):
    payload = "{\"total\":7525,\"per_page\":20,\"page\":%s,\"type\":\"\",\"scope\":\"\",\"sub_scope\":\"\",\"round\":\"\",\"valuation\":\"\",\"ipo_platform\":\"\",\"equity_ratio\":\"\",\"status\":\"\",\"prov\":\"\",\"city\":\"\",\"sort\":\"year_count\",\"time\":\"\",\"selected\":\"\",\"start_time\":\"\",\"end_time\":\"\"}" % pageNum
    try :
            response = requests.request('POST', url, headers=headers0, data=payload)
            ss = response.text.replace('\n', '')
            sss = json.loads(ss)['data']['data']
            print(str(sss))
            return sss

    except requests.exceptions.ConnectionError:
            print('遇到了反爬虫2，休息10秒')
            headers = getHeaders()
            time.sleep(10 + random.random() * 5)
            headers = getHeaders()
            get_invest_info(pageNum=pageNum, headers=headers)

    except KeyError:
            print('遇到了反爬虫3，休息10秒,重新生成headers')
            headers = getHeaders()
            print('》》》', headers['Cookie'])
            # time.sleep(10 + random.random() * 5)
            get_invest_info(pageNum=pageNum, headers=headers)


if __name__ == '__main__':
    pageNum = 1
    while pageNum <= 377:
        try:
            print('爬取第' + str(pageNum) +'页')
            sss = get_invest_info(str(pageNum),headers0)
            with open("invest_id_name.txt",'a',encoding='utf-8') as file:
                for s in sss:
                    file.write(str(s['id']) +','+ s['name'] +'\n')


            print(str(pageNum) +'爬取成功')
            pageNum = pageNum +1
        except TypeError as e:
            pass
            print(e)
    else:
        print('爬虫结束')
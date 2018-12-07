import requests
import json
# https://www.itjuzi.com/api/investments/45
# #投资轮次：
# data.investment_round
# #投资领域
# data.scope
# #单个项目投资规模
# data.single_investment_scale
# 机构类型：
# data.prop
# 管理资本规模：
# data.regulate_capital
# 机构名称：
#
# data.name
# 基金管理方：
# data.gp_info
# 官网地址：data.url
# https://www.itjuzi.com/api/invst_left_info/2
# 历史投资：data.invse_num
# 机构成员：data.invsp_num
# 地址：data.address
# 微信：data.wechat
# 电话：data.tel
# 邮箱：data.email

headers = {

"Host": "www.itjuzi.com",
"Connection": "keep-alive",
"Accept": "application/json, text/plain, */*",
"Authorization": "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3d3dy5pdGp1emkuY29tL2FwaS9hdXRob3JpemF0aW9ucyIsImlhdCI6MTU0NDE0NjgxOCwiZXhwIjoxNTQ0MjMzMjE4LCJuYmYiOjE1NDQxNDY4MTgsImp0aSI6ImFBcnFUTzYwdzlQS0VvNEoiLCJzdWIiOjY3NjM3NCwicHJ2IjoiMjNiZDVjODk0OWY2MDBhZGIzOWU3MDFjNDAwODcyZGI3YTU5NzZmNyJ9.EqR2rjoAAwMEVKGKQaVRHdzYmLhhJux8L2PQWuHPT3Y",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
"Referer": "https://www.itjuzi.com/investfirm/2",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-CN,zh;q=0.9",
"Cookie": "acw_tc=76b20f4515440837484458596eaf97ecc7efd719a2e8b8fd47ea7eb486a137; gr_user_id=8cff0e21-7ada-4206-8d78-d6d528b10e5b; _ga=GA1.2.1298098159.1544083754; _gid=GA1.2.838980469.1544083754; gr_session_id_eee5a46c52000d401f969f4535bdaa78=ebcde1f3-b775-4eaf-9ba8-53494d96f4f9; gr_session_id_eee5a46c52000d401f969f4535bdaa78_ebcde1f3-b775-4eaf-9ba8-53494d96f4f9=true; flag=676374-chen193713@sina.com-"

}

url = "https://www.itjuzi.com/api/investments/2"
url2 = "https://www.itjuzi.com/api/invst_left_info/2"


response = requests.request('GET',url,headers=headers)
response2 = requests.request('GET',url2,headers=headers)
try:
   com_touzilunci = json.loads(response.text)['data']['investment_round']
   # if com_touzilunci:
   #      for lunci  in  com_touzilunci:
   #          print(str(lunci['name']).replace('&nbsp;',''))
except KeyError:
   com_touzilunci = ''
try :
    com_touzilingyu = json.loads(response.text)['data']['scope']
    # if com_touzilingyu:
    #     for lingyu in com_touzilingyu:
    #         print(lingyu['name'])
except KeyError:
    com_touzilingyu = ''


try :
    com_single_touziguimo = json.loads(response.text)['data']['single_investment_scale']
    # if com_single_touziguimo:
    #     for k,v in com_single_touziguimo.items():
    #         print(k + ',' +v)
    print(str(com_single_touziguimo).replace(',',';').rstrip('}').lstrip('{'))
except:
    com_single_touziguimo =''

try:
    com_jigouleixing = json.loads(response.text)['data']['prop']
except:
    com_jigouleixing = ''

try:
    com_guanlizibenguimo = json.loads(response.text)['data']['regulate_capital']
except:
    com_guanlizibenguimo=''
try:
    com_jigoumingcheng = json.loads(response.text)['data']['name']
except:
    com_jigoumingcheng = ''
try:
    com_jijinguanlifang = json.loads(response.text)['data']['gp_info']
except:
    com_jijinguanlifang=''
try:
    com_url = json.loads(response.text)['data']['url']
except:
    com_jijinguanlifang = ''
try:
    com_lishitouzi = json.loads(response2.text)['data']['invse_num']
except:
    com_lishitouzi = ''
try:
    com_jigouchengyuan = json.loads(response2.text)['data']['invsp_num']
except:
    com_jigouchengyuan = ''
try:
    com_dizhi = json.loads(response2.text)['data']['address']
except:
    com_dizhi = ''
try:
    com_weixin = json.loads(response2.text)['data']['wechat']
except:
    com_weixin = ''
try:
    com_dianhua = json.loads(response2.text)['data']['tel']
except:
    com_dianhua = ''
try:
    com_youxiang = json.loads(response2.text)['data']['email']
except:
    com_youxiang = ''


# print(com_touzilunci )
# print(com_touzilingyu )
print(com_single_touziguimo )
# print(com_jigouleixing )
# print(com_guanlizibenguimo )
# print(com_jigoumingcheng )
# print(com_jijinguanlifang )
# print(com_url )
# print(com_lishitouzi )
# print(com_jigouchengyuan )
# print(com_dizhi )
# print(com_weixin )
# print(com_dianhua )
# print(com_youxiang )
# #投资轮次：
# data.investment_round
# #投资领域
# data.scope
# #单个项目投资规模
# data.single_investment_scale
# 机构类型：
# data.prop
# 管理资本规模：
# data.regulate_capital
# 机构名称：
#
# data.name
# 基金管理方：
# data.gp_info
# 官网地址：data.url
# https://www.itjuzi.com/api/invst_left_info/2
# 历史投资：data.invse_num
# 机构成员：data.invsp_num
# 地址：data.address
# 微信：data.wechat
# 电话：data.tel
# 邮箱：data.email

#print(response2.text)


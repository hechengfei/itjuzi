import requests

url='http://icanhazip.com/'
res = requests.get(url,proxies={'http':'http://219.238.186.188:8118'})
res.cookies.get_dict()
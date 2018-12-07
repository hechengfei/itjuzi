
import re


i=0
file_object = open('C:\\Users\\Administrator\\Desktop\\itOrange\\itOrange.txt','r',encoding='utf-8')
for line in  file_object.readlines():
    i = i + 1
    with open('id.txt', 'a') as f:
        if re.findall(r"\"id\": (\d+),$",line):
           ss = re.findall(r"\"id\": (\d+),$", line)[0]

           f.write(ss +'\n')


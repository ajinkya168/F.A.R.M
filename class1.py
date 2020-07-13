#! /usr/bin/env python3
import os
import requests
import json
item = os.listdir('/data/feedback')
print(item)
d={}
for i in range(len(item)):
        print(item[i])
        p=open('/data/feedback/'+item[i],'r')
        content=p.readlines()
        d['title']=content[0].strip('\n')
        d['name']=content[1].strip('\n')
        d['date']=content[2].strip('\n')
        d['feedback']=content[3].strip('\n')
#       k=json.dumps(d,indent=4)
        print(d)
        url="http://35.226.76.206/feedback"
        response=requests.post(url, data=d)
        print(response.ok)
        print(response.status_code)



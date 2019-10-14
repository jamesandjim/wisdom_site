import requests
from requests_toolbelt import MultipartEncoder
from requests_toolbelt.utils import dump
import json

url = "http://192.168.0.201/person/add"
person = {"faceId": "8888", "valid_time_type": 0, "valid_start": 0, "valid": 60, "username": "叶敏刚", "idcard": "420124197802025936", "sex": 1, "nation": "汉", "state": 1, "wgId": 1}
facepose = {'x': 74, 'y': 97, 'w': 304, 'h': 402}


m = MultipartEncoder(
    fields={'person': json.dumps(person, ensure_ascii=False), 'image': ('out.jpg', open('out.jpg', 'rb'), 'image/jpeg'), 'facepose': json.dumps(facepose)}
)

r = requests.post(url, data=m, headers={"Content-Type": m.content_type})
print(r.json())
print(dump.dump_all(r).decode('utf-8'))

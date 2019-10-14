import requests
from requests_toolbelt.multipart import encoder
from requests_toolbelt.utils import dump, formdata
import json


url = "http://192.168.0.201/person/add"
person = {'faceId': '8888', 'valid_time_type': 0, 'valid_start': 0, 'valid': 60, 'username': 'james', 'idcard': '420124197802025936', 'sex': 1, 'nation': 'han', 'state': 1, 'wgId': 1}
facepose = {'x': 74, 'y': 97, 'w': 304, 'h': 402}
person1 = json.dumps(person)
print(person1)
print(type(person1))
print(json.dumps(person1))
facepose1 = json.dumps(facepose)
print(facepose1)

# m = MultipartEncoder(
#     fields={'person': json.dumps(person1), 'image': ('out.jpg', open('out.jpg', 'rb'), 'image/jpeg'), 'facepose': json.dumps(facepose1)},
#     boundary='-----------------------------' + str(random.randint(1e28, 1e29 - 1))
# )
def my_callback(monitor):
    # Your callback function
    pass

e = encoder.MultipartEncoder(
    fields={'person': person1, 'image': ('out.jpg', open('out.jpg', 'rb'), 'image/jpeg'), 'facepose': facepose1}
)
m = encoder.MultipartEncoderMonitor(e, my_callback)
r = requests.post(url, data=m, headers={'Content-Type': m.content_type, 'Referer': url})
print(r.json())
print(dump.dump_all(r).decode('utf-8'))

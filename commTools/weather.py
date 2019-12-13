import requests
import re


def getWeatherBycityName(name):
    param = {'city': name}
    r = requests.get('http://wthrcdn.etouch.cn/weather_mini', params=param)
    j = r.json()

    if j['status'] == 1000:
        current = j['data']['forecast'][0]
        return current


def getFengLi(s):
    rgx = re.compile("\<\!\[CDATA\[(.*?)\]\]\>")
    m = rgx.search(s)
    n = m.group(1)
    if n[0:1] == r'<':
        n = '风力小于%s' % n[1:]
    if n[0:1] == r'>':
        n = '风力大于%s' % n[1:]

    return n


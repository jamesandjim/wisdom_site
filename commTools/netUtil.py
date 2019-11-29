# -*- coding: GBK -*-
import os

def DisableNetwork():
     ''' disable network card '''
     result = os.system(u"netsh interface set interface 以太网 disable")
     if result == 1:
          print("disable network card failed")
     else:
          print("disable network card successfully")

def ping(ip):
    ''' ping 主备网络 '''
    with os.popen("ping %s" % ip) as p:
        r = p.read()

        if r.find('无法访问目标主机') != -1:
            return 'off'
        else:
            return 'on'

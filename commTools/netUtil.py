# -*- coding: GBK -*-
import os

def DisableNetwork():
     ''' disable network card '''
     result = os.system(u"netsh interface set interface ��̫�� disable")
     if result == 1:
          print("disable network card failed")
     else:
          print("disable network card successfully")

def ping(ip):
    ''' ping �������� '''
    with os.popen("ping %s" % ip) as p:
        r = p.read()

        if r.find('�޷�����Ŀ������') != -1:
            return 'off'
        else:
            return 'on'

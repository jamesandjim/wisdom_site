# -*- coding: GBK -*-
import os
import time
PING_RESULT = 0
NETWORK_RESULT = 0
def DisableNetwork():
     ''' disable network card '''
     result = os.system(u"netsh interface set interface ��̫�� disable")
     if result == 1:
          print("disable network card failed")
     else:
          print("disable network card successfully")
def ping():
    ''' ping �������� '''
    with os.popen("ping 192.168.0.202") as p:
        r = p.read()
        print(r)
        if r.find('�޷�����Ŀ������') != -1:

             print('NO')

        else:
             print('yes')

if __name__ == '__main__':
    while True:
       PING_RESULT = ping()
       if PING_RESULT == 0:
           time.sleep(20)
       else:
           # DisableNetwork()
           time.sleep(10)
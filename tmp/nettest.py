# -*- coding: GBK -*-
import os

exit_code = os.system('ping 192.168.0.256')
if exit_code == 0:
    print('ok')
else:
    print("no")
# coding:utf-8
"""
Name : ping_util.py
Author  : JJon
Time    : 2023/8/22 16:26
Desc:
"""

import datetime
import time
from ping3 import ping


def ping_util(host: str, wait: int):
    time.sleep(wait)
    result = f'{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}-{str(ping(host))[:9]}'
    return result

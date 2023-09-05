# coding:utf-8
"""
Name : file_util.py
Author  : JJon
Time    : 2023/8/23 9:38
Desc:
"""

import datetime
from global_config import BASE_DIR


def get_latest_log_name(**kwargs):
    try:
        host = kwargs['host']
        replaced_host_str = host.replace('.', '-')
        log_name_lst = [f.name for f in (BASE_DIR / f'logs').iterdir()
                        if f.is_file()
                        if replaced_host_str in f.name
                        if 'error' not in f.name]
    except KeyError:
        log_name_lst = [f.name for f in (BASE_DIR / f'logs').iterdir()
                        if f.is_file() and '.log' in f.name
                        if 'error' not in f.name]

    if len(log_name_lst) == 0:
        return None
    latest_log_datetime = datetime.datetime.fromtimestamp(0)
    latest_log_name = ''
    for log_name in log_name_lst:
        log_datetime = datetime.datetime.strptime(log_name.split('_')[1], '%Y%m%d%H%M%S')
        latest_log_name = log_name if log_datetime > latest_log_datetime else latest_log_name

    return str(latest_log_name)
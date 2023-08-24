# coding:utf-8
"""
Name : data_analyze.py
Author  : JJon
Time    : 2023/8/21 17:08
Desc:
"""

import pandas as pd
from global_config import BASE_DIR, pd_settings
from util.logger import log_init


def package_loss_analyze(**kwargs):
    if 'file_name' in kwargs.keys():
        if kwargs['file_name'] is None:
            logger = log_init(usage='error')
            logger.error('不存在日志文件，请执行一次ping程序以获取日志文件。')
            return None
        file_path = BASE_DIR / f"logs/{kwargs['file_name']}"

    latency_df = pd.read_csv(file_path, sep='-')
    latency_df.columns = ['datetime', 'latency']
    latency_df['datetime'] = pd.to_datetime(latency_df['datetime'], format='%Y%m%d%H%M%S')
    latency_df.set_index('datetime', inplace=True)
    latency_df['latency'] = pd.to_numeric(latency_df['latency'], errors='coerce')
    hourly_none_sum = latency_df.resample('H').apply(lambda x: (x.isnull()).sum())
    hourly_none_sum.index.name = '时间'
    hourly_none_sum = hourly_none_sum.rename(columns={'latency': '丢包数量'})

    if 'usage' in kwargs.keys():
        match kwargs['usage']:
            case 'top3' | 'min3':
                saved_data_path = ''
                analyse_data = None

                if kwargs['usage'] == 'top3':
                    analyse_data = hourly_none_sum.groupby(pd.Grouper(freq='D'), group_keys=False).apply(
                        lambda x: x.nlargest(3, '丢包数量'))
                    saved_data_path = BASE_DIR / 'Output/none_top3_hours.csv'

                elif kwargs['usage'] == 'min3':
                    analyse_data = hourly_none_sum.groupby(pd.Grouper(freq='D'), group_keys=False).apply(
                        lambda x: x.nsmallest(3, '丢包数量'))
                    saved_data_path = BASE_DIR / 'Output/none_min3_hours.csv'

                analyse_data.to_csv(saved_data_path)
                print(f'解析csv文件已保存至\n{saved_data_path}')
            case 'print':
                pd_settings()
                print(f'各小时丢包数：\n{hourly_none_sum}')

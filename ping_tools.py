# coding:utf-8
"""
Name : ping_tools.py
Author  : JJon
Time    : 2023/8/22 16:27
Desc:
"""

import argparse
from util.logger import log_init
from util.ping_util import ping_util
from util.file_util import get_latest_log_name
from util.data_analyze import package_loss_analyze
from global_config import DEFAULT_PING_IP


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='PingTools',
        description='A simple toolbox for ping commands.')

    subparsers = parser.add_subparsers(dest='func', help='Function type.')
    subparsers.required = True

    ping_parser = subparsers.add_parser('ping', help='Ping util.')
    ping_parser.add_argument('host', help='Host ip or name destination.', type=str, default=DEFAULT_PING_IP, nargs="?")
    ping_parser.add_argument('wait', help='Wait second after last ping request.', type=int, default=1, nargs="?")

    analyze_parser = subparsers.add_parser('loss', help='Analyse package loss data.')
    analyze_parser.add_argument('--filename', type=str, default=get_latest_log_name(), nargs="?")
    analyze_parser.add_argument('--type', type=str, default='print', nargs="?")

    args = parser.parse_args()
    # print(args)

    match args.func:
        case 'ping':
            dest_host = args.host
            wait_sec = args.wait
            logger = log_init(dest_host)
            while True:
                logger.info(ping_util(dest_host, wait_sec))
        case 'loss':
            package_loss_analyze(file_name=args.filename, usage=args.type)
        case _:
            logger = log_init(usage='error')
            err = AttributeError('Unknown function selected.')
            logger.error(err)
            raise err

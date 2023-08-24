from loguru import logger as loguru_logger
from global_config import BASE_DIR, PROJECT_NAME
import datetime


def log_init(dest_host='', usage='log_info'):
    cur_datetime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    if usage == 'log_info':
        log_path = BASE_DIR / f'logs/{PROJECT_NAME}_{cur_datetime}_{dest_host.replace(".", "-")}.log'
        loguru_logger.add(log_path, rotation="100 MB", format="{message}")
        return loguru_logger
    elif usage == 'error':
        log_path = str(BASE_DIR / f'logs/{PROJECT_NAME}_error.log')
        loguru_logger.add(log_path, rotation="100 MB")
        return loguru_logger
    else:
        raise AttributeError('Unknown log usage.')

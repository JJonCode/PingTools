from pathlib import Path
import pandas as pd

PROJECT_NAME = 'PingTools'

BASE_DIR = Path(__file__).parent
DEFAULT_PING_IP = '127.0.0.1'


def pd_settings():
    pd.set_option('max_colwidth', 200)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

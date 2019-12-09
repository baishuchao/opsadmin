import os
from websdk.consts import const

ROOT_DIR = os.path.dirname(__file__)
debug = True

# 数据库
DEFAULT_DB_DBHOST = os.getenv('DEFAULT_DB_DBHOST', '192.168.183.128')  # 修改
DEFAULT_DB_DBPORT = os.getenv('DEFAULT_DB_DBPORT', '3306')   # 修改
DEFAULT_DB_DBUSER = os.getenv('DEFAULT_DB_DBUSER', 'root')   # 修改
DEFAULT_DB_DBPWD = os.getenv('DEFAULT_DB_DBPWD', 'm9uSFL7duAVXfeAwGUSG')  # 修改
DEFAULT_DB_DBNAME = os.getenv('DEFAULT_DB_DBNAME', 'ops_admin')  # 默 认


settings = dict(
    databases={
        const.DEFAULT_DB_KEY: {
            const.DBHOST_KEY: DEFAULT_DB_DBHOST,
            const.DBPORT_KEY: DEFAULT_DB_DBPORT,
            const.DBUSER_KEY: DEFAULT_DB_DBUSER,
            const.DBPWD_KEY: DEFAULT_DB_DBPWD,
            const.DBNAME_KEY: DEFAULT_DB_DBNAME, }
    })


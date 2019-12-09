#!/usr/bin/env python
# 启动脚本

import fire
from tornado.options import define
from websdk.program import MainProgram
from apps.cmdb.applications import Application as CmdbApp
from settings import settings as app_settings

define("service", default='api', help="start service flag", type=str)


class MyProgram(MainProgram):
    def __init__(self, service='ops_admin', progressid=''):
        self.__app = None
        settings = app_settings
        if service == 'ops_admin':
            self.__app = CmdbApp(**settings)
        super(MyProgram, self).__init__(progressid)
        self.__app.start_server()


if __name__ == '__main__':
    fire.Fire(MyProgram)


"""
#master
python startup.py --service='ops_admin' --port=8055



"""




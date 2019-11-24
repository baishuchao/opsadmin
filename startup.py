#!/usr/bin/env python
# 启动脚本


import fire
from tornado.options import define
from websdk.program import MainProgram

define("service", default='api', help="start service flag", type=str)


class MyProgram(MainProgram):
    pass


if __name__ == '__main__':
    fire.Fire(MyProgram)





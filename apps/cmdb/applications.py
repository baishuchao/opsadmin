#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
role   : Application
"""
from websdk.application import Application as myApplication
from apps.cmdb.handlers.asset_server_handler import asset_server_urls



class Application(myApplication):
    def __int__(self, **settings):
        urls = []
        urls.extend(asset_server_urls)




if __name__ == '__main__':
    pass

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 主机管理
import json
from sqlalchemy import or_
from libs.base_handler import BaseHandler
import tornado.web
from libs.common import check_ip
from websdk.db_context import DBContext
from models.cmdb import Server
from websdk.web_logs import ins_log

class ServerHandler(BaseHandler):
    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        data = json.loads(self.request.body.decode("utf-8"))
        hostname = data.get('hostname', None)
        ip = data.get('ip', None)
        port = data.get('port', 22)
        idc = data.get('idc', None)
        admin_user = data.get('admin_user', None)
        region = data.get('region', None)
        state = data.get('state', 'new')
        detail = data.get('detail', None)

        if not hostname or not ip or not port:
            return self.write(dict(code=-1, msg='关键参数不能为空'))

        if not admin_user:
            return self.write(dict(code=-1, msg='管理用户不能为空'))

        if not check_ip(ip):
            return self.write(dict(code=-1, msg="IP格式不正确"))

        if not type(port) is int and int(port) >= 65535:
            return self.write(dict(code=-1, msg="端口格式不正确"))

        with DBContext('r') as session:
            exist_id = session.query(Server.id).filter(Server.hostname == hostname).first()
            exist_ip = session.query(Server.id).filter(Server.ip == ip).first()
        if exist_id or exist_ip:
            return self.write(dict(code=-2, msg='不要重复记录'))

        with DBContext('w', None, True) as session:
            new_server = Server(hostname=hostname, ip=ip, port=int(port), idc=idc,
                                admin_user=admin_user, region=region, state=state, detail=detail)

            session.add(new_server)
        return self.write(dict(code=0, msg='添加成功'))

    def put(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass


asset_server_urls = [
    (r"/v1/cmdb/server/", ServerHandler),
]

if __name__ == '__main__':
    pass

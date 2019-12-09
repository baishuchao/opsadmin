from sqlalchemy import Column, String, Integer, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import class_mapper
from datetime import datetime

Base = declarative_base()
def model_to_dict(model):
    model_dict = {}
    for key, column in class_mapper(model.__class__).c.items():
        model_dict[column.name] = getattr(model, key, None)
    return model_dict

class Server(Base):
    __tablename__ = 'asset_server'

    ### 服务器主要信息
    id = Column(Integer, primary_key=True, autoincrement=True)  # ID自增长
    hostname = Column('hostname', String(1000), nullable=False)  # 主机名称
    ip = Column('ip', String(32), index=True, nullable=False)
    port = Column('port', Integer, nullable=False)  # 端口
    idc = Column('idc', String(128))  # IDC
    admin_user = Column('admin_user', String(128))  # 管理用户
    region = Column('region', String(128))  # 区域
    state = Column('state', String(128))  # 状态
    detail = Column('detail', String(128))  # 备注
    create_time = Column('create_time', DateTime(), default=datetime.now)  # 创建时间
    update_time = Column('update_time', DateTime(), default=datetime.now, onupdate=datetime.now)  # 记录更新时间







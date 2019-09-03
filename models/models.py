#pyqt5与sqlalchemy无法配合使用（找不到好的资料，文件暂不用）

import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


engine = sqlalchemy.create_engine('sqlite:///../db/wisdom.db')
base = declarative_base(engine)


class Department(base):
    __tablename__ = 'wis_department'
    id = Column(Integer, primary_key=True, nullable=False)
    person = relationship('person')

    name = Column(String(30), nullable=False)
    memo = Column(String(50), nullable=True)


class Person(base):
    __tablename__ = 'wis_person'
    idNo = Column(String(18), primary_key=True, nullable=False)
    name = Column(String(10), nullable=False)
    gender = Column(Integer, nullable=False)
    nation = Column(String(10), nullable=False)
    birthday = Column(String(10), nullable=False)
    address = Column(String(80), nullable=False)
    idissue = Column(String(80), nullable=False)
    idperiod = Column(String(17), nullable=False)
    idphoto = Column(String(50), nullable=False)
    photo = Column(String(50), nullable=False)
    inf_photo = Column(String(50), nullable=True)
    userType = Column(Integer, nullable=False)
    dev_mac = Column(String(15), nullable=False)
    RegType = Column(Integer, nullable=False)
    user_id = Column(String(20), nullable=True)
    work_sn = Column(String(20), nullable=True)
    department = Column(Integer, ForeignKey('wis_department.id'), nullable=False)
    status = Column(Integer, nullable=False, default=0)


if __name__ == '__main__':
    base.metadata.create_all(engine)
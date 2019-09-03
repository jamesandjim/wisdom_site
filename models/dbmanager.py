#pyqt5与sqlalchemy无法配合使用（找不到好的资料，文件暂不用）
from sqlalchemy.orm import sessionmaker

from models import models


class PersonEn:
    def __init__(self):
        self.Session = sessionmaker(bind=models.engine)
        self.session = self.Session()
        self.persons = None

    def create_one(self, person):
        self.session.add(person)
        self.session.commit()

    def create_many(self, persons):
        self.session.add_all(persons)
        self.session.commit()

    def query_all(self):
        self.persons = self.session.query(models.Person)

    def query_byName(self, name):
        self.persons = self.session.query(models.Person).filter_by(name=name)

    def query_byIdNum(self, idNo):
        self.persons = self.session.query(models.Person).filter_by(idNo=idNo).first()

    def update(self, idNo, user_id):
        person = self.session.query(models.Person).filter_by(idNo=idNo).first()
        person.user_id = user_id
        person.work_sn = user_id

        self.session.commit()

    def del_person(self, idNo):
        person = self.session.query(models.Person).filter_by(idNo=idNo).first()
        self.session.delete(person)
        self.session.commit()



from sqlalchemy import Column, ForeignKey, Integer,String

from models.database import Base

class People(Base):
    __tablename__='intruder'

    id=Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    surname = Column(String(200), nullable=False)
    age = Column(Integer, nullable=False)
    nickname = Column(String(250), nullable=False)
    id_car = Column(Integer, ForeignKey('cars.id'))


    def __init__(self, full_name, age, nickname, id_car):
        self.name = full_name[0]
        self.surname=full_name[1]
        self.age=age
        self.nichname=nickname

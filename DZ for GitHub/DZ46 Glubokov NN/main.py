import os
from sqlalchemy import and_, or_, not_, desc, func, distinct, text
from models.database import DATABASE_NAME, Session
import create_database as db_creator

from models.intruder import Intruder
from models.cars import Cars

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

    session = Session()
    # print(session.query(Cars).count())
    # print(session.query(Intruder).first())

    # for it in session.query(Intruder).filter(and_(Intruder.age >= 25, Intruder.id_car >=20)):
    #     print(it)
    #
    # for it in session.query(Cars).filter(and_(Cars.car_power>=400, Cars.car_model.like('Nissan%'))):
    #     print(it)
    #
    # print(session.query(Cars).filter(Cars.car_model.notin_(['Mazda RX-7','Mitsubishi Motors Lancer','Ford Focus'])).all())

    # print(session.query(Cars).filter(Cars.car_model.in_(['Mazda RX-7','Mitsubishi Motors Lancer','Ford Focus'])).all())
    #
    # for it in session.query(Intruder).order_by(Intruder.name):
    #     print(it)

    # for it in session.query(Cars).join(Intruder).filter(and_(Cars.car_model.like('Nissan%'), Intruder.id>20)):
    #     print(it)

    # i = session.query(Cars).get(7)
    # print(i)
    # i.car_power=500
    # print(i)
    # session.add(i)
    # session.commit()

    # session.add(Cars(id=59, car_model='Lamorghini Gallardo', car_power=700))
    # for it in session.query(Cars):
    #     print(it)
    # session.commit()

    s=session.query(Cars).filter(Cars.id==57).all()

    session.delete(s[0])

    session.commit()
    for it in session.query(Cars):
        print(it)

    # for it in session.query(Lesson.lesson_title, Group.group_name).filter(and_(association_table.c.lesson_id==Lesson.id, association_table.c.group_id == Group.id, Group.group_name == 'MDA-9')):
    #     print(it)
    # for it in session.query(Lesson).filter(not_(Lesson.id>=3), not_(Lesson.lesson_title.like('М%'))):
    #     print(it)
    # print(session.query(Lesson).filter(Lesson.lesson_title is not None).all())
    # print(session.query(Lesson).filter(Lesson.lesson_title.in_(['Математика', 'Линейная алгебра'])).all())

    # print(session.query(Student).filter(Student.age.between(16,17)).all())
    # print(session.query(Student).filter(not_(Student.age.between(17, 24))).all())
    # for it in session.query(Student).filter(Student.age.like('1%')).limit(4).offset(3):
    #     print(it)
    # for it in session.query(Student).order_by(Student.surname):
    #     print(it)
    # for it in session.query(Student).order_by(Student.surname):
    #     print(it)
    # for it in session.query(Student).order_by(desc(Student.surname)):
    #     print(it)
    # for it in session.query(Student).join(Group).filter(Group.group_name == 'MDA-9'):
    #     print(it)
    # for it in session.query(func.count(Student.surname), Group.group_name).join(Group).group_by(Group.group_name):
    #     print(it)

    # for it in session.query(func.count(Student.surname), Group.group_name).join(Group).group_by(
    #         Group.group_name).having(func.count(Student.surname) < 25):
    # #     print(it)
    # for it in session.query(distinct(Student.age)):
    #     print(it)
    # for it in session.query(distinct(Student.age)).filter(Student.age<20):
    #     print(it)

    # i = session.query(Lesson).get(7)
    # i.lesson_title= 'Информатика'
    # session.add(i)
    # session.commit()

    # for it in session.query(Lesson):
    #     print(it)

    # session.add(Lesson(lesson_title = 'Физика'))
    # session.commit()
    # for it in session.query(Lesson):
    #     print(it)
    #
    # i = session.query(Lesson).filter(Lesson.lesson_title == 'Физика').all()
    # session.delete(i)
    # session.commit()
    #
    # for it in session.query(Lesson):
    #     print(it)

    # for it in session.query(Student).filter(text('surname like "М%"')).order_by(text('name, id desc')):
    #     print(it)

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .orm import get_base


Base = get_base()


class User(Base):
    """
    Модель "Пользователь"
    """
    __tablename__ = 'univer_users'

    id = Column('user_id', Integer, primary_key=True)
    username = Column('user_login', String(50))

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def __str__(self):
        return self.username


class Student(Base):
    """
    Модель "Студент"
    """
    __tablename__ = 'univer_students'

    id = Column('students_id', Integer, primary_key=True)
    user_id = Column('user_id', ForeignKey('univer_users.user_id'))
    user = relationship('User')
    status = Column('status', Integer)
    last_name = Column('students_sname', String(100))
    first_name = Column('students_name', String(100))
    middle_name = Column('students_father_name', String(100))
    email = Column('students_email', String(25))
    identify_code = Column('students_identify_code', String(50))

    def __repr__(self):
        full_name = ' '.join(filter(None, [self.last_name, self.first_name, self.middle_name]))

        return '<Student {}>'.format(full_name)
    
    def __str__(self):
        return ' '.join(filter(None, [self.last_name, self.first_name, self.middle_name]))


class Personnel(Base):
    """
    Модель "Сотрудник"
    """
    __tablename__ = 'univer_personal'

    id = Column('personal_id', Integer, primary_key=True)
    user_id = Column('user_id', ForeignKey('univer_users.user_id'))
    user = relationship('User')
    status = Column('status', Integer)
    last_name = Column('personal_sname', String(200))
    first_name = Column('personal_name', String(100))
    middle_name = Column('personal_father_name', String(100))
    work_email = Column('personal_work_email', String(50))
    identify_code = Column('personal_identification_number', String(150))

    def __repr__(self):
        full_name = ' '.join(filter(None, [self.last_name, self.first_name, self.middle_name]))

        return '<Personnel {}>'.format(full_name)
    
    def __str__(self):
        return ' '.join(filter(None, [self.last_name, self.first_name, self.middle_name]))
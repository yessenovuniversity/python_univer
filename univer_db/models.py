from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship

from .orm import get_base


Base = get_base()


class Stage(Base):
    """
    Модель "Уровень"
    """

    __tablename__ = 'univer_stage'

    id = Column('stage_id', Integer, primary_key=True)
    status = Column(Integer)
    name_kz = Column('stage_name_kz', String(200))
    name_ru = Column('stage_name_ru', String(200))
    name_en = Column('stage_name_en', String(200))

    def __repr__(self):
        return "<Stage {}>".format(self)
    
    def __str__(self):
        return self.name_ru


class Speciality(Base):
    """
    Модель "Специальность"
    """

    __tablename__ = 'univer_speciality'

    id = Column('speciality_id', Integer, primary_key=True)
    status = Column(Integer)
    faculty_id = Column(ForeignKey('univer_faculty.faculty_id'))
    faculty = relationship('Faculty')
    stage_id = Column(ForeignKey('univer_stage.stage_id'))
    stage = relationship('Stage')
    name_kz = Column('speciality_name_kz', String(200))
    name_ru = Column('speciality_name_ru', String(200))
    name_en = Column('speciality_name_en', String(200))
    code = Column('speciality_okpd', String(10))
    description_kz = Column('speciality_description_kz', String)
    description_ru = Column('speciality_description_ru', String)
    description_en = Column('speciality_description_en', String)
    result_ru = Column(String)
    result_kz = Column(String)
    result_en = Column(String)
    type = Column(Integer)

    def __repr__(self):
        return "<Speciality {}>".format(self)
    
    def __str__(self):
        return "{} - {}".format(self.code, self.name_ru)


class Subject(Base):
    """
    Модель "Дисциплина"
    """

    __tablename__ = 'univer_subject'

    id = Column('subject_id', Integer, primary_key=True)
    name_kz = Column('subject_name_kz', String(500))
    name_ru = Column('subject_name_ru', String(500))
    name_en = Column('subject_name_en', String(500))
    status = Column(Integer)

    def __repr__(self):
        return '<Subject {}>'.format(self.name_ru)
    
    def __str__(self):
        return self.name_ru


class EducType(Base):
    __tablename__ = 'univer_educ_type'

    id = Column('educ_type_id', Integer, primary_key=True)
    name_ru = Column('educ_type_name_ru', String(100))

    def __repr__(self):
        return '<EducType {}>'.format(self.name_ru)

    def __str__(self):
        return self.name_ru


class LangDivision(Base):
    """
    Модель "Языковый отдел"
    """

    __tablename__ = 'univer_lang_division'

    id = Column('lang_division_id', Integer, primary_key=True)
    name_ru = Column('lang_division_name_ru', String(100))

    def __repr__(self):
        return '<LangDivision {}>'.format(self.name_ru)
    
    def __str__(self):
        return self.name_ru


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


class Teacher(Base):
    """
    Модель "Преподаватель"
    """

    __tablename__ = 'univer_teacher'

    id = Column('teacher_id', Integer, primary_key=True)
    personnel_id = Column('personal_id', ForeignKey('univer_personal.personal_id'))
    personnel = relationship('Personnel')
    status = Column('status', Integer)

    def __repr__(self):
        return '<Teacher {}>'.format(self.personnel)
    
    def __str__(self):
        return str(self.personnel)


class EducPlan(Base):
    """
    Модель "Учебный план"
    """

    __tablename__ = 'univer_educ_plan'

    id = Column('educ_plan_id', Integer, primary_key=True)
    speciality_id = Column('speciality_id', ForeignKey('univer_speciality.speciality_id'))
    speciality = relationship(Speciality)
    year = Column('educ_plan_adm_year', Integer)

    def __repr__(self):
        return "<EducPlan {} {}>".format(self.speciality, self.year)
    
    def __str__(self):
        return "{} {}".format(self.speciality, self.year)


class EducPlanPos(Base):
    """
    Модель "Позиции учебного плана"
    """

    __tablename__ = 'univer_educ_plan_pos'

    id = Column('educ_plan_pos_id', Integer, primary_key=True)
    educ_plan_id = Column('educ_plan_id', ForeignKey('univer_educ_plan.educ_plan_id'))
    educ_plan = relationship('EducPlan')
    subject_id = Column('subject_id', ForeignKey('univer_subject.subject_id'))
    subject = relationship(Subject)
    semester = Column('educ_plan_pos_semestr', Integer)

    def __repr__(self):
        return "<EducPlanPos {}: {} ({} семестр)>".format(self.educ_plan, self.subject, self.semester)
    
    def __str__(self):
        return "{}: {} ({} семестр)".format(self.educ_plan, self.subject, self.semester)


class Attendance(Base):
    """
    Модель "Журнал посещаемости"
    """

    __tablename__ = 'univer_attendance'

    date = Column('att_date', Date, primary_key=True)
    grade = Column('ball', Float)
    was = Column(Boolean)
    student_id = Column(ForeignKey('univer_students.students_id'), primary_key=True)
    student = relationship(Student)
    group_id = Column(ForeignKey('univer_group.group_id'), primary_key=True)
    group = relationship('Group')

    def __repr__(self):
        return '<Attendance {}: {} балл ({})>'.format(self.student, self.grade, self.date)
    
    def __str__(self):
        return '{}: {} балл ({})'.format(self.student, self.grade, self.date)


class Group(Base):
    """
    Модель "Группа"
    """

    __tablename__ = 'univer_group'

    id = Column('group_id', Integer, primary_key=True)
    educ_plan_pos_id = Column('educ_plan_pos_id', ForeignKey('univer_educ_plan_pos.educ_plan_pos_id'))
    educ_plan_pos = relationship(EducPlanPos, backref='groups')
    teacher_id = Column('teacher_id', ForeignKey('univer_teacher.teacher_id'))
    teacher = relationship(Teacher)
    year = Column('group_year', Float)
    semester = Column('group_semestr', Integer)
    educ_type_id = Column('educ_type_id', ForeignKey('univer_educ_type.educ_type_id'))
    educ_type = relationship(EducType)
    lang_division_id = Column('lang_division_id', ForeignKey('univer_lang_division.lang_division_id'))
    lang_division = relationship(LangDivision)


class GroupStudent(Base):
    """
    Модель "Студент в группе"
    """

    __tablename__ = 'univer_group_student'

    id = Column('group_student_id', Integer, primary_key=True)
    group_id = Column(ForeignKey('univer_group.group_id'))
    group = relationship(Group, backref='group_students')
    student_id = Column(ForeignKey('univer_students.students_id'))
    student = relationship(Student)
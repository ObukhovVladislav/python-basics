class Student:
    def __init__(self):
        self.name = None
        self.surname = None
        self.patronymic = None
        self.group_number = None
        self.student_card = None
        self.gradebook = None


class Teacher:
    def __init__(self):
        self.name = None
        self.surname = None
        self.patronymic = None
        self.discipline = None


class Study_group:
    def __init__(self):
        self.number = None
        self.number_of_students = None
        self.specialty = None
        self.curator = None


class College:
    def __init__(self):
        self.college_name = None
        self.administration = None
        self.number_of_students = None
        self.specialties = None


class Exam:
    def __init__(self):
        self.mark = None
        self.teacher = None
        self.discipline = None
        self.student = None


class Student_on_the_exam:
    def __init__(self):
        self.mark = None
        self.teacher = None
        self.discipline = None
        self.gradebook = None


class Car:
    def __init__(self):
        self.engine = None
        self.color = None
        self.brand = None
        self.mark = None
        self.type = None


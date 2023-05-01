import json


class Student:
    def __init__(self, f_n, l_n):
        self.first_name = f_n
        self.last_name = l_n

    def get_info(self):
        return {'first name': self.first_name, 'last name': self.last_name}


std1 = Student("John", "Doe")


class Storage:

    def __init__(self):
        self.my_list = []

    def add(self, elem):
        self.my_list.append(elem)

    def get(self, string):
        if string == "":
            return sorted(self.my_list)[:5]
        else:
            return [elem for elem in self.my_list if string in elem]


class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def to_json(self):
        course_dict = {
            'name': self.name,
            'students': [student.info() for student in self.students]
        }
        return json.dumps(course_dict)

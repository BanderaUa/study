import pytest


class FileStorage:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = {}

    @staticmethod
    def create(file_path):
        return FileStorage(file_path)

    def load_data(self):
        try:
            with open(self.file_path, 'r') as file:
                self.data = eval(file.read())
        except FileNotFoundError:
            self.data = {}

    def save_data(self):
        with open(self.file_path, 'w') as file:
            file.write(repr(self.data))

    def add_course(self, course_name):
        self.data[course_name] = []

    def add_student_to_course(self, course_name, student):
        if course_name in self.data:
            self.data[course_name].append(student)

    def remove_course(self, course_name):
        if course_name in self.data:
            del self.data[course_name]

    def remove_student_from_course(self, course_name, student):
        if course_name in self.data:
            if student in self.data[course_name]:
                self.data[course_name].remove(student)

    def get_students_in_course(self, course_name):
        if course_name in self.data:
            return self.data[course_name]
        return []

    def get_courses(self):
        return list(self.data.keys())


class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def get_students(self):
        return self.students


@pytest.fixture
def file_storage():
    file_path = "test_data.txt"
    file_storage = FileStorage.create(file_path)
    file_storage.load_data()
    return file_storage


def test_add_course(file_storage):
    course_name = "Math"
    file_storage.add_course(course_name)
    courses = file_storage.get_courses()
    assert course_name in courses


def test_remove_course(file_storage):
    course_name = "Math"
    file_storage.add_course(course_name)
    file_storage.remove_course(course_name)
    courses = file_storage.get_courses()
    assert course_name not in courses


def test_add_student_to_course(file_storage):
    course_name = "Math"
    student = "John Doe"
    file_storage.add_course(course_name)
    file_storage.add_student_to_course(course_name, student)
    students = file_storage.get_students_in_course(course_name)
    assert student in students


def test_remove_student_from_course(file_storage):
    course_name = "Math"
    student = "John Doe"
    file_storage.add_course(course_name)
    file_storage.add_student_to_course(course_name, student)
    file_storage.remove_student_from_course(course_name, student)
    students = file_storage.get_students_in_course(course_name)
    assert student not in students


if __name__ == "__main__":
    file_path = "data.txt"  # шлях до файлу, де будуть зберігатися дані

    file_storage = FileStorage.create(file_path)
    file_storage.load_data()

    app = App(file_storage)
    app.run()

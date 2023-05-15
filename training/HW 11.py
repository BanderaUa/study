import unittest

class Pagination:
    def __init__(self, data):
        self.data = data
        self.page_size = 3
        self.current_page = 0

    def get_current_page_data(self):
        start_index = self.current_page * self.page_size
        end_index = start_index + self.page_size
        return self.data[start_index:end_index]

    def next_page(self):
        if self.current_page < len(self.data) // self.page_size:
            self.current_page += 1

    def previous_page(self):
        if self.current_page > 0:
            self.current_page -= 1


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

    def get_students(self):
        return self.students


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_data.txt"
        self.file_storage = FileStorage.create(self.file_path)
        self.file_storage.load_data()

    def tearDown(self):
        self.file_storage.save_data()

    def test_data_structure(self):
        expected_data = {}
        self.assertEqual(self.file_storage.data, expected_data)

        course_name = "Math"
        self.file_storage.add_course(course_name)
        expected_data[course_name] = []

        self.assertEqual(self.file_storage.data, expected_data)

    def test_get_courses(self):
        course_names = ["Math", "Physics", "Chemistry"]
        expected_courses = []
        for course_name in course_names:
            self.file_storage.add_course(course_name)
            expected_courses.append(course_name)

        courses = self.file_storage.get_courses()
        self.assertEqual(courses, expected_courses)


class TestPagination(unittest.TestCase):
    def test_pagination(self,):
        data = [1, 2, 3, 4]

        pagination = Pagination(data)

        page_data = pagination.get_current_page_data()
        expected_data = [1, 2, 3]
        self.assertEqual(page_data, expected_data)

        pagination.next_page()
        page_data = pagination.get_current_page_data()
        expected_data = [4]
        self.assertEqual(page_data, expected_data)

        pagination.next_page()
        page_data = pagination.get_current_page_data()



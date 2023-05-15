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
        self.data[course_name] = None

    def get_courses(self):
        return list(self.data.keys())


class App:
    def __init__(self, file_storage):
        self.file_storage = file_storage

    def run(self):
        while True:
            print("Меню:")
            print("1. Додати курс")
            print("2. Показати всі курси")
            print("3. Вийти з програми")

            choice = input("Виберіть опцію: ")

            if choice == "1":
                course_name = input("Введіть назву курсу: ")
                self.file_storage.add_course(course_name)
                print("Курс успішно додано.")
            elif choice == "2":
                courses = self.file_storage.get_courses()
                print("Список курсів:")
                for course in courses:
                    print(course)
            elif choice == "3":
                self.file_storage.save_data()
                print("Дані збережено. Програма завершується.")
                break
            else:
                print("Невірний пункт меню. Спробуйте ще раз.")



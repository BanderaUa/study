import json


class JsonReader:
    def __init__(self, json_str):
        self.json_str = json_str

    def __enter__(self):
        self.data = json.loads(self.json_str)
        return self.data

    def __exit__(self, exc_type, exc_value, traceback):
        pass


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'


class Rectangle:
    def __init__(self, upper_left, lower_right):
        self.upper_left = upper_left
        self.lower_right = lower_right

    def contains_point(self, point):
        return (self.upper_left.x <= point.x <= self.lower_right.x and
                self.upper_left.y <= point.y <= self.lower_right.y)

    def __contains__(self, point):
        return self.contains_point(point)

    def __str__(self):
        return f'Rectangle({self.upper_left}, {self.lower_right})'

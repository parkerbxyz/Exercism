from collections import defaultdict


class School:
    def __init__(self):
        self.students = defaultdict(set)

    def add_student(self, name: str, grade: int):
        self.students[grade].add(name)

    def roster(self):
        return [name for k, v in sorted(self.students.items()) for name in sorted(v)]

    def grade(self, grade_number):
        return sorted(list(self.students[grade_number])) or []

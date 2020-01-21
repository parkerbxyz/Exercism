from typing import List

PLANTS = {
        'C': 'Clover',
        'G': 'Grass',
        'R': 'Radishes',
        'V': 'Violets',
    }

STUDENTS = [
        'Alice', 'Bob', 'Charlie', 'David',
        'Eve', 'Fred', 'Ginny', 'Harriet',
        'Ileana', 'Joseph', 'Kincaid', 'Larry'
    ]


class Garden:
    def __init__(self, diagram, students=STUDENTS):
        self.rows = diagram.splitlines()
        self.students = sorted(students)

    def plants(self, student: str) -> List[str]:
        index = self.students.index(student) * 2
        return [PLANTS[p[i]] for p in self.rows for i in (index, index + 1)]

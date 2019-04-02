class Matrix:
    def __init__(self, matrix_string):
        self.row_list = [list(map(int, row.split()))
                         for row in matrix_string.splitlines()]
        self.col_list = list(map(list, zip(*self.row_list)))

    def row(self, index):
        return self.row_list[index - 1]

    def column(self, index):
        return self.col_list[index - 1]

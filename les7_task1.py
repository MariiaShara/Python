class Matrix:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.list_of_lists])

    def __add__(self, other):
        result = []
        numbers = []
        for i in range(len(self.list_of_lists)):
            for j in range(len(self.list_of_lists[0])):
                numbers.append(self.list_of_lists[i][j] + other.list_of_lists[i][j])
                if len(numbers) == len(self.list_of_lists[0]):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)


matrix_1 = Matrix([[1, 2, 3], [3, 4, 5], [0, 4, 1]])
print(matrix_1)

matrix_2 = Matrix([[2, 8, 4], [9, 7, 6], [3, 5, 0]])
print(matrix_2)

print(matrix_1 + matrix_2)

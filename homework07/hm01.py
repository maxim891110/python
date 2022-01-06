class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matrix_i = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        for i in range(len(self.list_1)):

            for x in range(len(self.list_2)):
                matrix_i[i][x] = self.list_1[i][x] + self.list_2[i][x]

        return str("\n".join(["\t".join([str(x) for x in i]) for i in matrix_i]))

    def __str__(self):
        return str("\n".join(["\t".join([str(x) for x in i]) for i in matrix_i]))


my_matrix = Matrix([[5, 18, 11], [6, 17, 23], [41, 50, 9]], [[54, 8, 2], [6, 7, 8], [24, 5, 97]])

print(my_matrix.__add__())

class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matr = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                matr[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

    def __str__(self, matr=None):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))


my_matrix = Matrix([[4, 1, 7],
                    [6, 7, 2],
                    [1, 5, 9]],
                   [[4, 8, 2],
                    [6, 7, 9],
                    [2, 5, 7]])

print(my_matrix.__add__())

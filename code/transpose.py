from matrix import Matrix

mat = [ [0.49, 0.97, 0.53, 0.05, 0.33],
        [0.65, 0.62, 0.51, 1.00, 0.38],
        [0.61, 0.45, 0.74, 0.27, 0.64],
        [0.17, 0.36, 0.17, 0.96, 0.12],
        [0.79, 0.32, 0.68, 0.90, 0.77] ]

#mat = [1, 2, 3, 4, 5, 6]
'''
mat = [[1],
        [2],
        [3],
        [4],
        [5],
        [6]]
'''

def print_matrix(matrix):
  rows = len(matrix)

  for r in range(rows):
    print(matrix[r])

my_matrix = Matrix(mat)
my_matrix.print()

print()

m = my_matrix.transpose()
my_matrix.print()
'''
print()

m = my_matrix.transpose()
my_matrix.print()

print()

my_matrix.print()
'''

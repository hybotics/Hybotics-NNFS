#!/usr/bin/env python3

def print_matrix(mat):
  rows = len(mat)
  
  for r in range(rows):
    print(mat[r])

mat = [ [0.49, 0.97, 0.53, 0.05, 0.33, 0.21],
        [0.65, 0.62, 0.51, 1.00, 0.38, 0.71],
        [0.61, 0.45, 0.74, 0.27, 0.64, 0.51],
        [0.17, 0.36, 0.17, 0.96, 0.12, 0.41],
        [0.62, 0.20, 0.47, 0.25, 0.81, 0.11],
        [0.11, 0.39, 0.18, 0.91, 0.16, 0.31],
        [0.79, 0.32, 0.68, 0.90, 0.77, 0.61] ]

rows = len(mat)
cols = len(mat[0])

erows = cols
ecols = rows
print(f"Start Dims = {rows} x {cols}")
print(f"Final Dims = {erows} x {ecols}")
print()

r = -1
new_mat = []

print("<Start>")
print_matrix(mat)
print()

print("Start Matrix Transform")
while r < erows - 1:
  r += 1

  new_row = []
  c = -1

  while c < ecols - 1:
    c += 1

    #print(f"<3> Position = {r} x {c}")

    new_row.append(mat[c][r])

    #print(f"<4> ({r}) New Row = {new_row}")

  if r < erows:
    new_mat.append(new_row)

print()
print("<5> Starting Matrix =")
print_matrix(mat)
print()
print("<5> Transformed Matrix =")
print_matrix(new_mat)

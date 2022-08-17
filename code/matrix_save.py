class Matrix():
  def __init__(self, mat):
    self.rows = len(mat)

    try:
      self.cols = len(mat[0])
    except TypeError:
      self.rows = 1
      self.cols = len(mat)
      
    print(f"<init> rows = {self.rows}, cols = {self.cols}")

    self.matrix = mat

  def _save(self, m):
    self.old_matrix = self.matrix
    self.matrix = m
    self.rows = len(m)

    try:
      self.cols = len(m[0])
    except TypeError:
      self.rows = 1
      self.cols = len(m)

  def transpose(self):
    new_mat = []
    new_row = []
    rows = self.rows
    cols = self.cols
    
    print(f"<2> Input array dimensions are {rows} x {cols}")
    print()

    # Standard list (1 dimension array)
    if rows == 1:
      for c in range(cols):
        new_row.append([self.matrix[c]])
        
      rows = len(new_row)
      cols = 1
      new_mat = new_row
    elif cols == 1:
      for r in range(rows):
        new_row.append(self.matrix[r][0])
      
      new_mat = new_row
    else:
      for r in range(rows):
        new_row = []

        for c in range(cols):
          print(f"<3> Position = {r} x {c}")
          new_row.append(self.matrix[c][r])
          print(f"<4> ({r}) New Row = {new_row}")

        print()
        new_mat.append(new_row)
        
      print(f"<5> New Matrix = {new_mat}")

    self._save(new_mat)

    return new_mat

  def print(self):
    print()
    print("Printing final output...")
    
    if self.rows == 1:
      print(self.matrix)
    else:
      for row in range(self.rows):
        print(self.matrix[row])

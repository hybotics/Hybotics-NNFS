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

  def _print(self, mat):
    print()
    print("<Debug> Printing the array...")
    
    if self.rows == 1:
      print(mat)
    else:
      for row in range(len(mat)):
        print(mat[row])

  def transpose(self):
    new_mat = []
    new_row = []
    rows = self.rows
    cols = self.cols
    
    print(f"<2> Input array dimensions are {rows} x {cols}")
    print(f"    Output array should be {cols} x {rows}")
    print()

    if rows == 1:
      # Standard list (1 dimension array)
      for c in range(cols):
        new_row.append([self.matrix[c]])
        
      rows = len(new_row)
      cols = 1
      new_mat = new_row
    elif cols == 1:
      # Standard single column
      for r in range(rows):
        new_row.append(self.matrix[r][0])
      
      new_mat = new_row
    else:
      # This should handle everything else
      r = 0

      while r < rows:
        new_row = []
        c = 0

        while c < cols:          
          print(f"<3> Position = {r} x {c}")

          try:
            new_row.append(self.matrix[c][r])
          except IndexError:
            print(f"<Error> Position = {r} x {c}")
            self._print(new_mat)
            print(new_row)
            raise
            
          print(f"<4> ({r}) New Row = {new_row}")
          
          c += 1

        print()
        new_mat.append(new_row)

        r += 1
        
        if r >= rows:
          break
        
      print(f"<5> New Matrix = {new_mat}")

    self._save(new_mat)

    return new_mat

  def print(self):
    print()
    print("Printing array...")
    
    if self.rows == 1:
      print(self.matrix)
    else:
      for row in range(self.rows):
        print(self.matrix[row])

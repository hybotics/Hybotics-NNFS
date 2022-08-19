import re

class Matrix():
  def __init__(self, mat_a=None, mat_b=None):
    self.init = True
    
  def _dims(self, mat):
    rows = len(mat)

    try:
      cols = len(mat[0])
    except TypeError:
      # Special case for a regular [] list
      rows = 1
      cols = len(mat)
      
    return rows, cols

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

  def dot(self, mat_a, mat_b):
    r_sum = 0.0
    result = []

    a_rows, a_cols = self._dims(mat_a)
    b_rows, b_cols = self._dims(mat_b)

    if a_rows != b_cols:
      raise ValueError("The rows the first matrix must be the same as the colums of the second matrix")

    for a_r in range(a_rows):
      r_sum = 0.0
      new_r = []
        
      for b_r in range(b_rows):
        print(f"Position: ({a_r} x {b_r}) * ({b_r} x {a_r})")
        r_sum += (mat_a[a_r][b_r] * mat_b[b_r][a_r])
        
      print(f"r_sum = {r_sum}")
      new_r.append(r_sum)

      result.append(new_r)

    return result

  def transpose(self, mat):
    new_mat = []
    new_row = []

    rows, cols = self._dims(mat)

    if rows == 1:
      # Standard list (1 dimension array)
      for c in range(cols):
        new_row.append([mat[c]])
        
      rows = len(new_row)
      cols = 1
      new_mat = new_row
    elif cols == 1:
      # Standard single column
      for r in range(rows):
        new_row.append(mat[r][0])
      
      new_mat = new_row
    else:
      # This should handle everything else
      r = 0

      while r < cols:
        new_row = []
        c = 0

        while c < rows:          
          new_row.append(mat[c][r])
          
          c += 1

        new_mat.append(new_row)

        r += 1

    #self._save(new_mat)

    return new_mat

  def print(self, mat, text=""):
    txt = f"Printing the {text} matrix."
    txt = re.sub(r'[\s]+', ' ', txt)
    print(txt)
    
    rows, cols = self._dims(mat)
    
    if rows == 1:
      print(mat)
    else:
      for row in range(rows):
        print(mat[row])

import re

class Matrix():
  def __init__(self, mat):
    self.rows = len(mat)

    try:
      self.cols = len(mat[0])
    except TypeError:
      # Special case for a regular [] list
      self.rows = 1
      self.cols = len(mat)

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

      while r < cols:
        new_row = []
        c = 0

        while c < rows:          
          new_row.append(self.matrix[c][r])
          
          c += 1

        new_mat.append(new_row)

        r += 1

    self._save(new_mat)

    return new_mat

  def print(self, text=""):
    print()
    txt = f"Printing {text} array..."
    txt = re.sub(r'[\s]+', ' ', txt)
    print(txt)
    
    if self.rows == 1:
      print(self.matrix)
    else:
      for row in range(self.rows):
        print(self.matrix[row])

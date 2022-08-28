def dot_product(p1, p2):
  plen = len(p1)

  if len(p2) != plen:
    raise ValueError("The length of the inputs must be the same!")

  dprod = 0.0

  for el_nr in range(plen):
    dprod += (p1[el_nr] * p2[el_nr])

  return dprod


def multiplication_table(n):
     """
     Return an n x n multiplication table as a list of rows (lists).
     Each row i (1..n) should contain:
     [i*1, i*2, ..., i*n]
     If n < 0, raise ValueError.
     If n is not an int, raise TypeError.
     """
     multiplestable = []

     if n < 0:
          raise ValueError("n is less than zero")
     elif type(n) != int:
          raise TypeError("Invalid Data type")
     else:
          for i in range(1,n+1):
               multiples = []
               for j in range(1, n+1):
                    multiples.append(i*j)
               multiplestable.append(multiples)

     return multiplestable

def hailstone(n):
  """
  Returns a list which is the hailstone sequence starting from n and ending
  at 1.
  >>> hailstone(5)
  [5, 16, 8, 4, 2, 1]
  """
  l = [n]
  while n > 1:
    if n % 2 == 0:
      n /= 2
    else:
      n = 3*n + 1
    l.append(n)
  return l 

def sequence(N):
  """
  Given a number N, return a list of the lengths of the hailstone sequences
  of the numbers from 1 to N.
  >>> sequence(4)
  [1, 2, 8, 3]
  """
  l = []
  i = 1
  while i <= N:
    l.append(len(hailstone(i)))
    i = i + 1
  return l 

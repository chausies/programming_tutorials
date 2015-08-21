def sort(l):
  """
  Returns a list which is a sorted version of l.
  >>> a = list(range(10))
  >>> from random import shuffle
  >>> shuffle(a)
  >>> sort(a)
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  """
  a = list(l)
  n = len(a)
  in_order = False
  while not in_order:
    i = 0 
    switched = False
    while i < n-1: 
      if a[i] > a[i+1]:
        switched = True
        a[i], a[i+1] = a[i+1], a[i]
      i = i + 1
    if switched == False:
      in_order = True
  return a


def most_common(l):
  """
  Given a list l, returns the most common element of that list.
  >>> l = ["a", 1, 3, 1, 3, "a", "b", 1]
  >>> most_common(l)
  1
  """
  d = {}
  for x in l:
    if not x in d.keys():
      d[x] = 0
    d[x] = d[x] + 1
  most = 0
  key = None
  for k in d.keys():
    if d[k] > most:
      most = d[k]
      key = k
  return key

def unique_items(l):
  """
  Given a list l, returns the number of unique elements in that list.
  >>> l = [1, 2, "a", 2, "a", 1, 3]
  >>> unique_items(l)
  4
  """
  d = []
  for x in l:
    if not x in d:
      d.append(x)
  return len(d)

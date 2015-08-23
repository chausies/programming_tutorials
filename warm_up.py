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

def max_f(l_f):
  """Returns a function which is the max of provided functions.

  Arguements
  ----------
  l_f : list of functions
    A list of functions of one variable

  Returns
  ------
  f : a function of one variable
    f(x) returns the max value of all the funtions in l_f applied to x

  Example
  -------
  >>> y_1 = lambda x : x
  >>> y_2 = lambda x: -x
  >>> l_f = [y_1, y_2]
  >>> a = max_f(l_f)
  >>> a(7)
  7
  >>> a(-7)
  7
  """
  def fun(x):
    largest = None
    for f in l_f:
      if largest == None:
        largest = f(x) 
      elif f(x) > largest:
        largest = f(x)
    return largest
  return fun

def split_string(string):
  """Splits a string into an array of words.

  Walks through `string` and splits it into an array of words, where the
  words were separated by a space (" ") in the original string.

  Example
  -------
  >>> string = "Hello, how are you doing?"
  >>> split_string(string) + 1
  ['Hello,', 'how', 'are', 'you', 'doing?']
  """
  return "NOT YET IMPLEMENTED"

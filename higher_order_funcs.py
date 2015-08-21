def apply_func(f, l):
  """
  Given a list l, returns a new list where every element x of l has been
  replaced with f(x).
  >>> f = lambda x : x**2
  >>> l = [1, 2, 3, 4]
  >>> apply_func(f, l)
  [1, 4, 9, 16]
  """
  a = []
  for x in l:
    a.append(f(x))
  return a

def find_avg(experiment, N=10000):
  """
  Returns the sample average over N trials of calling experiment().
  >>> from random import random as rand
  >>> experiment = lambda : rand()<.5
  >>> round(find_avg(experiment), 2)
  0.5
  """
  s = 0
  i = 0
  while i < N:
    s += experiment()
    i = i + 1
  return s/float(N)

def apply_all(l_f):
  """
  Given a list of functions l_f, returns a function that applies them all
  successively.
  >>> square = lambda x : x**2
  >>> one_minus = lambda x : 1 - x
  >>> sqrt = lambda x : x**.5
  >>> l_f = [square, one_minus, sqrt]
  >>> circ = apply_all(l_f)
  >>> round(circ(sqrt(3)/2), 2)
  0.5
  """
  def f(x):
    for g in l_f: 
      x = g(x)
    return x
  return f

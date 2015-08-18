from random import random as rand

def dice():
  """
  Returns a number uniformly at random between 1 and 6.
  >>> dice() in [1, 2, 3, 4, 5, 6]
  True
  """
  r = rand()
  i = 1.0
  while i <= 6:
    if r < i/6:
      return i 
    i = i + 1

def sample_avg(N):
  """
  Returns the sample average of N independent samples of dice()
  >>> round(sample_avg(10000), 1)
  3.5
  """
  a = 0
  i = 0
  while i < N:
    a += dice()
    i = i + 1
  return a/N

def k_in_a_row(k, N=10000):
  """
  Returns the average number of flips to get k heads in a row over N
  samples.
  >>> round(k_in_a_row(1), 1)
  2.0
  """
  a = 0
  i = 0
  while i < N:
    a += helper(k)
    i = i + 1
  return a/float(N)

def helper(k):
  t = 0
  f = 0
  while t < k:
    f = f + 1
    if rand() > 0.5:
      t = t + 1
    else:
      t = 0
  return f


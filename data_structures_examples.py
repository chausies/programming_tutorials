#-----------------#
#  List examples  #
#-----------------#

# Lists hold a bunch of objects in them, whether they be ints, strs,
# floats, or whatever. 

l = [1, 2, 1, 3.14159, "pi", "anh"]

print "l = " + str(l)

# example of several useful list thingies:

# list length
print "length of l is " + str(len(l))

# index a list
print "3rd element of l is " + str(l[3])

# append to a list
l.append(1)

print "l is now " + str(l)

# reverse a list
l.reverse()
print "l is now " + str(l)

#----------------#
#  List Problem  #
#----------------#

# Given a list l, return a new list with just the first two and last two
# elements in l. You may assume l has at least 4 elements in it.

def prob1(l):
  # YOUR CODE HERE
  return [l[0], l[1], l[len(l)-2], l[len(l)-1]]

l = ["hey", "mickey", "you're", "so", "fine", "you're", "so", "fine", "you", "blow", "my", "mind"]
ans = prob1(l)
print "First 2 and last 2 elements of l are " + str(ans)


# Given a list of numbers l, "smooth" it by replacing each element with the
# average of itself and its 2 adjacent elements, and return this new
# smoothed list s. You can assume that a 0 is adjacent to the first and
# last elements of l.

def smooth(l):
  s = []
  i = 0
  while i < len(l):
    a = l[i-1]
    b = l[i]
    c = l[min(i+1, len(l)-1)]
    if i == 0:
      a = 0
    elif i == len(l)-1:
      c = 0
    s.append((a + b + c)/3.0)
    i += 1
  return s

l = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]
s = smooth(l)
print "smoothing " + str(l) + " yields " + str(s)


# Next, using your smooth() function, write another function that, given a
# list l, smoothes it k times

def multi_smooth(l, k=1):
  s = l
  i = 0
  while i < k:
    s = smooth(s)
    i = i + 1
  return s

l = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]
s = multi_smooth(l, 5)
print "smoothing " + str(l) + " 5 times over yields " + str([ round(100*x)/100 for x in s])




#-----------------------#
#  Dictionary examples  #
#-----------------------#

def list2dic(l):
  """
  Given a list l, returns a dictionary d such that l[2*i]=>l[2*i+1] for all
  i.
  >>> l = ["a", 1, "b", 2, "c", 3]
  >>> print list2dic(l) == {'a': 1, 'b': 2, 'c': 3}
  True
  """
  d = {}
  i = 0
  while i < len(l):
    d[l[i]] = l[i+1]
    i = i + 2
  return d

#----------------------#
#  Dictionary Problem  #
#----------------------#

# Given a string s, return a dictionary d where the keys are all the
# letters occuring in s and the values are the number of times those
# letters appear

def prob2(s):
  s = s.lower() # make sure all the letters in s are lowercase
  d = {}
  for c in s:
    if c in d:
      d[c] = d[c] + 1
    else:
      d[c] = 1
  for k in d.keys():
    d[k] /= float(len(s))
    d[k] = round(d[k]*100)
  return d

s = "Silly Sally sells seashells on the seashore"
ans = prob2(s)
print "Answer for problem 2: " + str(ans)
print sum(ans.values())

def reverse_dict(d):
  """
  Given a dictionary d, returns a new dictionary t so that entries (e.g. k:
  v) in the original dictionary are flipped (e.g. v: k) in the new
  dictionary. If multiple keys in d have the same value (e.g. k1: v, k2: v), 
  then make the value point to a list of those keys (e.g. v: [k1, k2]) in t.
  >>> d = {"a": 1, "b": 2, "c": 3, "d": 1}
  >>> t = reverse_dict(d)
  >>> expected_t = {1: ['a', 'd'], 2: 'b', 3: 'c'}
  >>> print t == expected_t
  True
  """
  t = {}
  for k in d.keys():
    v = d[k]
    if not v in t:
      t[v] = [k]
    else:
      t[v] = t[v] + [k]
  for k in t.keys():
    if len(t[k]) == 1:
      t[k] = t[k][0]
  return t

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
  return "NOT YET IMPLEMENTED"

l = ["hey", "mickey", "you're", "so", "fine", "you're", "so", "fine", "you", "blow", "my", "mind"]
ans = prob1(l)
print "First 2 and last 2 elements of l are " + str(ans)


# Given a list of numbers l, "smooth" it by replacing each element with the
# average of itself and its 2 adjacent elements, and return this new
# smoothed list s. You can assume that a 0 is adjacent to the first and
# last elements of l.

def smooth(l):
  # YOUR CODE HERE
  return "NOT YET IMPLEMENTED"

l = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]
s = smooth(l)
print "smoothing " + str(l) + " yields " + str(s)


# Next, using your smooth() function, write another function that, given a
# list l, smoothes it k times

def multi_smooth(l, k=1):
  # YOUR CODE HERE
  return "NOT YET IMPLEMENTED"

l = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]
s = multi_smooth(l, 5)
print "smoothing " + str(l) + " 5 times over yields " + str(s)



#-----------------------#
#  Dictionary examples  #
#-----------------------#



#----------------------#
#  Dictionary Problem  #
#----------------------#

# Given a string s, return a dictionary d where the keys are all the
# letters occuring in s and the values are the number of times those
# letters appear

def prob2(s):
  s = s.lower() # make sure all the letters in s are lowercase
  # YOUR CODE HERE
  return "NOT YET IMPLEMENTED"

s = "Silly Sally sells seashells on the seashore"
ans = prob2(s)
print "Answer for problem 2: " + str(ans)

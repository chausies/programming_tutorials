#----------------------#
#  While Loop Example  #
#----------------------#

# Find the largest integer k less than N such that k is divisible by both 
# a and b

def ex1(N, a, b):
  largest = 0
  k = 1
  while k < N:
    if (k % a == 0) and (k % b == 0):
      largest = k
    k = k + 1
  return largest


ans = ex1(9876, 39, 51)
print "The largest number less than 9876 that's divisible by both 39 and 51 is " + str(ans)

#-------------#
#  Problem 1  #
#-------------#

# Find the largest integer k less than N such that k is divisible by every
# element in the list l

def prob1(N, l):
  largest = 0
  k = 1
  while k < N:
    valid = True
    for a in l:
      if (k % a != 0):
        valid = False
    if valid:
      largest = k
    k = k + 1 
  return largest

ans = prob1(88888, [5, 7, 9, 10])
print "The largest number less 88888 that's divisible by 5, 7, 9 and 10 is " + str(ans)

#--------------------#
#  For Loop Example  #
#--------------------#

# Count the number of times the letter C appears in a string

def ex2(string, C):
  string = string.lower() # make every character in the string lowercase
  C = C.lower()           # make sure the character C is in lowercase
  amt = 0 
  for char in string: # for each character in the string
    if char == C:     # if the character is C
      amt = amt + 1   # then the amount of times you've seen C increases by one
  return amt

tongue_twister = "Silly Sally sells seashells on the seashore."
ans = ex2(tongue_twister, 's')
print "The number of s's in the silly-sally tongue twister is " + str(ans)

#-------------#
#  Problem 2  #
#-------------#

# L is a list of lists. Find the longest list l in L, and then return the
# largest element of l

def prob2(L):
  largest_len = 0
  largest_list = None
  for l in L:
    if len(l) > largest_len:
      largest_len = len(l) 
      largest_list = l 
  largest_k = 0
  for k in l:
    if k > largest_k:
      largest_k = k
  return largest_k


L = [ [8, 9, 10], [5], [1, 5, 3, 6] ]
print "The answer for Problem 2 is " + str(prob2(L)) # should be 6


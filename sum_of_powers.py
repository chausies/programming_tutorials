# Find the largest integer N such that the sum 1**p + 2**p + ... + N**p is
# less than D digits for D from 1-10 and p from 2-6

def sum_of_powers(N, p):
	l = range(1,N+1)
	l2 = range (1,6)
	s = 0
	for x in l: 
		s = x**p + s 
	return s

def f(D,p):
	N = 1
	while len(str(sum_of_powers(N,p))) < D:
		N = N + 1
	return N - 1
for p in range(2,6):
    l = []
    for D in range(1,11):
		l = l + [f(D,p)]
    print l

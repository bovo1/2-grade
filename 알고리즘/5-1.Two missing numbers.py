import math

def ns(n):
	result = n*(n+1)//2
	return result

def n2_s(n):
	tmp = 0
	for i in range(1, n+1):
		tmp = tmp + (i**2)
	return tmp

def guess_two_missing_numbers(n, S, T):
	# code here
	ns_ab = ns(n) - S
	square_ab = n2_s(n) - T
	multi_ab = (ns_ab**2 - square_ab)//2
	
	a = abs(((-1 * ns_ab) + math.sqrt(ns_ab*ns_ab - 4 * multi_ab))//2)
	b = abs(((-1 * ns_ab) - math.sqrt(ns_ab*ns_ab - 4 * multi_ab))//2)
	
	a = int(a)
	b = int(b)
	
	if a>b:
		return b,a
	else:
		return a,b

n = int(input())
S, T = [int(x) for x in input().split()]
a, b = guess_two_missing_numbers(n, S, T)
print(a, b)

def find_median_five(L):
	o_max = L[0]
	t_max = L[0]
	th_max = L[0]
	
	for i in L:
		if i > o_max:
			th_max = t_max
			t_max = o_max
			o_max = i
		else:
			if i > t_max:
				th_max = t_max
				t_max = i
			elif i < t_max:
				th_max = i
	return th_max

def MoM(L, k): # L의 값 중에서 k번째로 작은 수 리턴
	if len(L) == 1: # no more recursion
		return L[0]
	i = 0
	A, B, M, medians = [], [], [], []
	while i+4 < len(L):
		medians.append(find_median_five(L[i: i+5]))
		i+=5
	if i < len(L) and i+4 >= len(L):
		medians.append(find_median_five(L[i:]))
	
	mom = MoM(medians, len(medians)//2)
	#print(mom)
	for v in L:
		if v < mom: A.append(v)
		elif v > mom: B.append(v)
		else: M.append(v)
				
	if len(A) >= k: return MoM(A, k)
	elif (len(A) + len(M)) < k : return MoM(B, k-len(A)-len(M))
	else: return mom
			
# n과 k를 입력의 첫 줄에서 읽어들인다
# n개의 정수를 읽어들인다. (split 이용 + int로 변환)
n,k = [int(x) for x in input().split()]
L = [int(x) for x in input().split()]
print(MoM(L, k))
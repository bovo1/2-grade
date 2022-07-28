def reconstruct(B):
	# B로부터 A를 재구성해 리턴
	# 이 함수를 작성합니다~
	X = []
	n = len(B)
	A = [0]*n
	
	for i in range(n):
		X.insert(B[i], i)
	
	for i in range(n):
		A[X[i]] = i	
		
	return A

B = [int(x) for x in input().split()]
A = reconstruct(B)
print(A)

# 1. 본인이 작성한 알고리즘의 수행시간을 간략히 분석해보자
# n^2 + 2n + 2, 메인 문 포함 n^2 + 3n +4
# 2. 수행시간 T(n)을 Big-O료 표기해보자
# O(n^2)

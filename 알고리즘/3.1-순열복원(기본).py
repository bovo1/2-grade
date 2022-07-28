def reconstruct(S, L):
	# S, L로부터 A를 재구성해 리턴
	# 이 함수를 작성합니다~
	n = len(S)
	A = [0]*n
	for i in range(n):
		A[i] = S[i]
		if L[i] >= 0 and (n-(i+1)) >= L[i]:
			A[i] = A[i] + ((n-(i+1)) - L[i])
	return A
	
# S와 L을 차례로 읽어들임
S = [int(x) for x in input().split()]
L = [int(x) for x in input().split()]
A = reconstruct(S, L)
print(A)

# 1. 본인이 작성한 알고리즘의 수행시간을 간략히 분석해보자
# 7n +1, 메인 문 포함이면 9n + 3
# 2. 수행시간 T(n)을 Big-O료 표기해보자
# O(n)

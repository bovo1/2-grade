import time, random

def evaluate_n2(A, x):
	# code for O(n^2)-time function
	L = []
	R = []
	for i in range(len(A)):
		L.append(x)
	L[0] = 1

	for i in range(2, len(A)):
		for j in range(i, len(A)):
			L[j] *= L[1]
	
	for i in range(len(A)):
		R.append(A[i] * L[i])
	#print(R)
	#print(sum(R))

	
def evaluate_n(A, x):
	# code for O(n)-time function
	renew = x
	R = []
	R.append(A[0] * 1)
	for i in range(1, len(A)):
		R.append(A[i] * renew)
		renew *= x
		
	#print(R)
	#print(sum(R))
	
	
	
random.seed()		# random 함수 초기화
# n 입력받음
n = int(input())
A = []
#리스트 A를 randint를 호출하여 n개의 랜덤한 숫자로 채움
for i in range(n):
	A.append(random.randint(-999, 999))
#print(A)
	
before_n2 = time.clock()
# evaluate_n2 호출
evaluate_n2(A, n)
after_n2 = time.clock()

before_n = time.clock()
# evaluate_n 호출
evaluate_n(A, n)
after_n = time.clock()
# 두 함수의 수행시간 출력
print("evaluate_n2의 수행 시간: ", (after_n2 - before_n2))
print("evaluate_n의 수행 시간: ", (after_n - before_n))

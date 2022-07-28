class Heap:
	
	def __init__(self, L=[]):
		self.A = L
	def __str__(self):
		return str(self.A)
	def __len__(self):
		return len(self.A)

	def Mheapify_down(self, k, n):
		while 2*k+1 < n:
			L, R = 2*k+1, 2*k+2
			if self.A[L] > self.A[k]:	#k의 왼쪽 자식 노드가 k 노드보다 값이 크면?
				m = L
			else:
				m = k
			if R < n and self.A[R] > self.A[m]:
				m = R
			if m != k:
				self.A[k], self.A[m] = self.A[m], self.A[k]
				k=m
			else:
				break
				
	def mheapify_down(self, k, n):
		while 2*k+1 < n:
			L, R = 2*k+1, 2*k+2
			if self.A[L] < self.A[k]:	#k의 왼쪽 자식 노드가 k 노드보다 값이 작으면?
				m = L
			else:
				m = k
			if R < n and self.A[R] < self.A[m]:
				m = R
			if m != k:
				self.A[k], self.A[m] = self.A[m], self.A[k]
				k=m
			else:
				break
	
	def Mheapify_up(self, k):	
		while k > 0 and self.A[(k-1)//2] < self.A[k] :
			self.A[k], self.A[(k-1)//2] = self.A[(k-1)//2], self.A[k]
			k = (k-1)//2

	def mheapify_up(self, k):	
		while k > 0 and self.A[(k-1)//2] > self.A[k] :
			self.A[k], self.A[(k-1)//2] = self.A[(k-1)//2], self.A[k]
			k = (k-1)//2

	def Minsert(self, key):
		self.A.append(key)
		self.Mheapify_up(len(self.A)-1)

	def minsert(self, key):
		self.A.append(key)
		self.mheapify_up(len(self.A)-1)
	
	def Mdelete(self):
		self.A[0], self.A[len(self.A)-1] = self.A[len(self.A)-1], self.A[0]
		self.A.pop()
		self.Mheapify_down(0, len(self.A))

	def mdelete(self):
		self.A[0], self.A[len(self.A)-1] = self.A[len(self.A)-1], self.A[0]
		self.A.pop()
		self.mheapify_down(0, len(self.A))
		
	def medium(self,Min,S):
		self.A.append(S[0])	#처음 기준이 되는 것. 기준은 이동할때 마다 바뀜.
		m_sum = S[0]
		for k in range(1, len(S)):
			if self.A[0] > S[k]:
				self.Minsert(S[k])
			else:
				Min.minsert(S[k])
			
			if len(self.A) > len(Min.A)+1:
				Min.minsert(self.A[0])
				self.Mdelete()
			elif len(self.A) < len(Min.A):
				self.Minsert(Min.A[0])
				Min.mdelete()
			
			m_sum += self.A[0]
		print(m_sum)
			
S = [int(x) for x in input().split()]
max_list, min_list = [], []
Max = Heap(max_list)
Min = Heap(min_list)
Max.medium(Min,S)

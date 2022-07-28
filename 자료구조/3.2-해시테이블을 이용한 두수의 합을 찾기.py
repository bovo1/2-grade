class HashOpenAddr:
	def __init__(self, n):
		size = int(len(n) * float(1.5))
		self.size = size
		self.keys = [None]*self.size

	def find_slot(self, key):
		i = self.hash_function(key)
		start = i
		while self.keys[i] != None and self.keys[i] != key:
			i = (i+1) % self.size
			if (i == start): return None
		return i
	
	def set(self, key):
		i = self.find_slot(key)
		if i == None : return None
		else:
			self.keys[i] = key
		return key
	
	def hash_function(self, key):
		return key % self.size
	
def plus(k,n):
	H = HashOpenAddr(n)
	A = []
	i = 0
	#해시테이블에 n 값 넣음.
	while True:
		H.set(int(n[i]))
		if i == len(n)-1:break
		i += 1
	#print(H)
	a,count = -1,0	
	while a+1 != len(n):
		a += 1
		if H.keys[a] == None:
			continue
		else:
			o = H.find_slot(int(k-H.keys[a]))
			if o == None or H.keys[o] == None:
				continue
			elif H.keys[a] == H.keys[o]:
				continue
				#print("a=", H.keys[a], "o", o)
			A.append(a)
			A.append(o)
			#print("a=",H.keys[a], "o=", H.keys[o])
		A1 = set(A)
		count = int(len(A1)/2)
	return count
	
k = int(input())
n = input().split()
print(plus(k,n))


class Node:
	def __init__(self, key = None):
		self.key = key
		self.next = self
		self.prev = self
	
	def __str__(self):
		return str(self.key)

class DoublyLinkedList:
	def __init__(self):
		self.head = Node()
		self.size = 0
	
	def __len__(self):
		return self.size
	
	def splice(self, a, b, x):
		if a == None or b == None or x == None:
			return
		ap = a.prev
		bn = b.next
		ap.next = bn
		bn.prev = ap
		
		xn = x.next
		xn.prev = b
		b.next = xn
		a.prev = x
		x.next = a
		self.size += 1
	
	def moveAfter(self,a, x):
		self.splice(a, a, x)
	
	def moveBefore(self, a, x):
		self.splice(a, a, x.prev)
	
	def insertAfter(self, x, key):
		self.moveAfter(Node(key), x)
	
	def insertBefore(self, x, key):
		self.moveBefore(Node(key), x)

	def pushBack(self, key):
		self.insertBefore(self.head, key)
		
	def remove(self, x):
		if x == None or x == self.head: return
		x.prev.next = x.next
		x.next.prev = x.prev
		self.size -= 1
		
def josephus(n, k):
	L = DoublyLinkedList()
	i = 1
	while True:
		L.pushBack(i)
		if(i==n): break
		i += 1

	v = L.head.next
	count = 1
	while L.size > 1:	
		if count == k:
			if v == L.head:
				L.remove(v.next)
				count = 1
				v = v.next
			else:
				L.remove(v)
				v = v.next
				count = 1
				if v == L.head:
					v = v.next
		else:
			v = v.next
			if v == L.head:
				count = count
			else:
				count += 1
	return v.__str__()

n, k = map(int, input().split())
print(josephus(n, k))

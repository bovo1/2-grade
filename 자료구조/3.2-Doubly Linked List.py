# 1. class Node 선언 부분
class Node:
	def __init__(self, key = None):
		self.key = key
		self.next = self
		self.prev = self
	
	def __str__(self):
		return str(self.key)

# 2. class DoublyLinkedList 선언부분
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

	def search(self, key):
		v = self.head.next
		while v != self.head:
			if v.key == key:
				return v
			v = v.next
		return None
	
	def isEmpty(self):
		if self.head.next == self.head:
			return True
		else:
			return False
	
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
		
	def pushFront(self, key):
		self.insertAfter(self.head, key)
		
	def deleteNode(self, x):
		if x == None or x == self.head: return
		x.prev.next = x.next
		x.next.prev = x.prev
		self.size -= 1
		
	def popBack(self):
		if self.isEmpty():
			return None
		key = self.head.prev.key
		self.deleteNode(self.head.prev)
		return key
	
	def popFront(self):
		if self.isEmpty():
			return None
		key = self.head.next.key
		self.deleteNode(self.head.next)
		return key
		
	def first(self):
		if self.isEmpty():
			return None
		else:
			return self.head.next
	
	def last(self):
		if self.isEmpty():
			return None
		else:
			return self.head.prev
	
	""""def split(self, x):
		A = DoublyLinkedList()
		v = A.head
		n = self.search(x)
		if n == None:
			return None
		self.splice(x, self.head.prev, v)
		return A
	
	def join(self, A):
		v = A.head.next
		c = A.head.prev
		self.splice(v, c, self.head.prev)"""

	def printList(self):
		v = self.head.next
		print("h -> ", end='')
		while v != self.head:
			print(v.key, "->", end=" ")
			v = v.next
		print("h")
			

L = DoublyLinkedList()
while True:
    cmd = input().split()
    if cmd[0] == 'pushF':
        L.pushFront(int(cmd[1]))
        print("+ {0} is pushed at Front".format(cmd[1]))
    elif cmd[0] == 'pushB':
        L.pushBack(int(cmd[1]))
        print("+ {0} is pushed at Back".format(cmd[1]))
    elif cmd[0] == 'popF':
        key = L.popFront()
        if key == None:
            print("* list is empty")
        else:
            print("- {0} is popped from Front".format(key))
    elif cmd[0] == 'popB':
        key = L.popBack()
        if key == None:
            print("* list is empty")
        else:
            print("- {0} is popped from Back".format(key))
    elif cmd[0] == 'search':
        v = L.search(int(cmd[1]))
        if v == None: print("* {0} is not found!".format(cmd[1]))
        else: print(" * {0} is found!".format(cmd[1]))
    elif cmd[0] == 'insertA':
        # inserta key_x key : key의 새 노드를 key_x를 갖는 노드 뒤에 삽입
        x = L.search(int(cmd[1]))
        if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
        else:
            L.insertAfter(x, int(cmd[2]))
            print("+ {0} is inserted After {1}".format(cmd[2], cmd[1]))
    elif cmd[0] == 'insertB':
        # inserta key_x key : key의 새 노드를 key_x를 갖는 노드 앞에 삽입
        x = L.search(int(cmd[1]))
        if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
        else:
            L.insertBefore(x, int(cmd[2]))
            print("+ {0} is inserted Before {1}".format(cmd[2], cmd[1]))
    elif cmd[0] == 'delete':
        x = L.search(int(cmd[1]))
        if x == None:
            print("- {0} is not found, so nothing happens".format(cmd[1]))
        else:
            L.deleteNode(x)
            print("- {0} is deleted".format(cmd[1]))
    elif cmd[0] == "first":
        print("* {0} is the value at the front".format(L.first()))
    elif cmd[0] == "last":
        print("* {0} is the value at the back".format(L.last()))
    elif cmd[0] == 'print':
        L.printList()
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")

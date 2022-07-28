class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None
        self.height = 0  # 높이 정보도 유지함에 유의!!

    def __str__(self):
        return str(self.key)

class BST:
    def __init__(self):
        self.root = None
        self.size = 0
    def __len__(self):
        return self.size

    def preorder(self, v):
        if v != None:
            print(v.key, end=' ')
            self.preorder(v.left)
            self.preorder(v.right)

    def inorder(self, v):
        if v != None:
            self.inorder(v.left)
            print(v.key, end=' ')
            self.inorder(v.right)

    def postorder(self, v):
        if v != None:
            self.postorder(v.left)
            self.postorder(v.right)
            print(v.key, end=' ')


    def find_loc(self, key):
        if self.size == 0:
            return None
        p = None
        v = self.root
        while v != None:
            if v.key == key: return v
            elif v.key < key:
                p = v
                v = v.right
            else:
                p = v
                v = v.left
            p.height += 1
        return p

    def search(self, key):
        v = self.find_loc(key)
        if v == None:
            return None
        else: return v

    def maxnode(self):
        v = self.root
        while v.right != None:
            v = v.right
        return v
    
    def minnode(self):
        v = self.root
        while v.left != None:
            v = v.left
        return v

    def update_height(self):
        v = self.root
        Mnode = self.maxnode()
        Mnode.height = 0
        mnode = self.minnode()
        mnode.height = 0
        while Mnode.parent != v:
            Mnode = Mnode.parent
            Mnode.height += 1
            if Mnode.left != None:
                while Mnode.left != None:
                    Mnode.left.height += 1
                    Mnode.left = Mnode.left.left
        
        while mnode.parent != v:
            mnode = mnode.parent
            mnode.height += 1
            if mnode.right != None:
                while mnode.right != None:
                    mnode.right.height += 1
                    mnode.right = mnode.right.right

    def insert(self, key):
        # 노드들의 height 정보 update 필요!!!!!!!!!!!
        p = self.find_loc(key)
        if p == None or p.key != key:
            v = Node(key)
            if p == None:
                self.root = v
            else:
                v.parent = p
                if p.key >= key:
                    p.left = v
                else:
                    p.right = v
            self.size += 1
            return v
        else:
            return None
        self.update_height()
    
            
    def deleteByMerging(self, x):
	    # assume that x is not None
	    a, b, pt = x.left, x.right, x.parent
	    if a == None: c = b
	    else: # a != None
		    c = m = a
		    # find the largest leaf m in the subtree of a
		    while m.right:
			    m = m.right
		    m.right = b
		    if b: b.parent = m
	
	    if self.root == x: # c becomes a new root
		    if c: c.parent = None
		    self.root = c
	    else:		# c becomes a child of pt of x
		    if pt.left == x: pt.left = c
		    else: pt.right = c
		    if c: c.parent = pt
	    self.size -= 1

    def deleteByCopying(self, x):
        a = x.left
        b = x.right
        pt = x.parent
        if a != None:
            m = a
            while m.right:
                m = m.right
        elif a == None and b != None:
            m = b
            while m.left:
                m = m.left
        else:
            m = None

        if m == None:
            if pt == None:
                self.root = None
            else:
                if pt.right == x:
                    pt.right = None
                else:
                    pt.left = None
            self.size -= 1

        else:
            ml = m.left
            mr = m.right
            mp = m.parent

            x.key = m.key
            if b != None and a == None:
                if mr == None:
                    if mp.right == m:
                        mp.right = None
                    else:
                        mp.left = None
                elif mr != None:
                    if mp.right == m:
                        mr.parent = mp
                        mp.right = mr
                    else:
                        mr.parent = mp
                        mp.left = mr

            elif a != None:
                if ml == None:
                    if mp.right == m:
                        mp.right = None
                    else:
                        mp.left = None
                elif m1 != None:
                    if mp.right == m:
                        ml.parent = mp
                        mp.right = ml
                    else:
                        ml.parent = mp
                        mp.left = ml
            self.size -= 1

    def height(self, x): # 노드 x의 height 값을 리턴
        if x == None: return -1
        else: return x.height

    def pred(self, x): # key값의 오름차순 순서에서 x.key 값의 다음 노드(successor) 리턴
        # x의 successor가 없다면 (즉, x.key가 최대값이면) None 리턴
        x = x.left
        if x != None: 
            while x.right != None:
                if x.right == None: 
                    return x 
                else: 
                    x = x.right
        return x

    def succ(self, x): # key값의 오름차순 순서에서 x.key 값의 이전 노드(predecssor) 리턴
        # x의 predecessor가 없다면 (즉, x.key가 최소값이면) None 리턴
        x = x.right
        if x != None: # just a sanity check 
            while x.left != None:
                if x.left == None: 
                    return x 
                else: 
                    x = x.left
        return x

    def rotateLeft(self, z): # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
        x = z.right             
        if x == None:
            return
        b = x.left             
        x.parent = z.parent
        if z.parent:
            if z.parent.right == z:
                z.parent.right = x
            else: 
                z.parent.left = x
        if x: x.left = z
        z.parent = x 
        z.right = b
        if b: b.parent = z
        # z == self.root라면 x가 새로운 루트가 되어야 함!
        if z == self.root and z != None:
            self.root = x

	# [주의] height가 있다면 x와 z의 height 값을 수정하는 코드 추가 필요
    def rotateRight(self, z): # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
        x = z.left	             # assume that z != None 
        if x == None: return     # if x == None: nothing changed
        b = x.right              # b == None 인 경우도 가능
        x.parent = z.parent
        if z.parent:
            if z.parent.left == z:
                z.parent.left = x
            else: 
                z.parent.right = x
        if x: x.right = z
        z.parent = x 
        z.left = b
        if b: b.parent = z
        # z == self.root라면 x가 새로운 루트가 되어야 함!
        if z == self.root and z != None:
            self.root = x
	# [주의] height가 있다면 x와 z의 height 값을 수정하는 코드 추가 필요
	
T = BST()
while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        v = T.insert(int(cmd[1]))
        print("+ {0} is inserted".format(v.key))
    elif cmd[0] == 'deleteC':
        v = T.search(int(cmd[1]))
        T.deleteByCopying(v)
        print("- {0} is deleted by copying".format(int(cmd[1])))
    elif cmd[0] == 'deleteM':
        v = T.search(int(cmd[1]))
        T.deleteByMerging(v)
        print("- {0} is deleted by merging".format(int(cmd[1])))
    elif cmd[0] == 'search':
        v = T.search(int(cmd[1]))
        if v == None:
            print("* {0} is not found!".format(cmd[1]))
        else:
            print("* {0} is found!".format(cmd[1]))
    elif cmd[0] == 'height':
        h = T.height(T.search(int(cmd[1])))
        if h == -1:
            print("= {0} is not found!".format(cmd[1]))
        else:
            print("= {0} has height of {1}".format(cmd[1], h))
    elif cmd[0] == 'succ':
        v = T.succ(T.search(int(cmd[1])))
        if v == None:
            print("> {0} is not found or has no successor".format(cmd[1]))
        else:
            print("> {0}'s successor is {1}".format(cmd[1], v.key))
    elif cmd[0] == 'pred':
        v = T.pred(T.search(int(cmd[1])))
        if v == None:
            print("< {0} is not found or has no predecssor".format(cmd[1]))
        else:
            print("< {0}'s predecssor is {1}".format(cmd[1], v.key))
    elif cmd[0] == 'Rleft':
        v = T.search(int(cmd[1]))
        if v == None:
            print("@ {0} is not found!".format(cmd[1]))
        else:
            T.rotateLeft(v)
            print("@ Rotated left at node {0}".format(cmd[1]))
    elif cmd[0] == 'Rright':
        v = T.search(int(cmd[1]))
        if v == None:
            print("@ {0} is not found!".format(cmd[1]))
        else:
            T.rotateRight(v)
            print("@ Rotated right at node {0}".format(cmd[1]))
    elif cmd[0] == 'preorder':
        T.preorder(T.root)
        print()
    elif cmd[0] == 'postorder':
        T.postorder(T.root)
        print()
    elif cmd[0] == 'inorder':
        T.inorder(T.root)
        print()
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")

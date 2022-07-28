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
        self.balance = 0

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
        return p

    def search(self, key):
        v = self.find_loc(key)
        if v == None:
            return None
        else: return v

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
            
    def deleteByMerging(self, x):
        a, b, pt = x.left, x.right, x.parent
        if a == None:
            c = b
            s = pt
        else:
            c = m = a
            while m.right:
                m = m.right
            m.right = b
            if b: b.parent = m
            s = m
	
        if self.root == x:
            if c: c.parent = None
            self.root = c
        else:
            if pt.left == x: pt.left = c
            else: pt.right = c
            if c: c.parent = pt
        self.size -= 1
        return s

    def deleteByCopying(self, x):
        a = x.left
        b = x.right
        pt = x.parent
        if a != None:
            m = a
            while m.right:
                m = m.right
            s = m
        elif a == None and b != None:
            m = b
            while m.left:
                m = m.left
            s = m
        else:
            m = None
            s = pt

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
                elif ml != None:
                    if mp.right == m:
                        ml.parent = mp
                        mp.right = ml
                    else:
                        ml.parent = mp
                        mp.left = ml
            self.size -= 1
        return s


    def height(self, node):
        if node == None:
            return -1
        else:
            lh = self.height(node.left)
            rh = self.height(node.right)
            return max(lh, rh) + 1

    def succ(self, node):
        successor = None
        v = self.root
        if v == None:
            return None
        while v != None:
            if v.key > node.key:
                successor = v
                v = v.left
            else:
                v = v.right
        return successor

    def pred(self, node):
        predecessor = None
        v = self. root
        if v == None:
            return None
        while v != None:
            if v.key < node.key:
                predecessor = v
                v = v.right
            else:
                v = v.left
        return predecessor
    
    def rotateRight(self, node):
        if not node: return
        x = node.left
        if x == None: return
        b = x.right
        x.parent = node.parent
        if node.parent:
            if node.parent.left == node:
                node.parent.left = x
            else:
                node.parent.right = x
        x.right = node
        node.parent = x
        node.left = b
        if b:
            b.parent = node
        if self.root == node and node != None:
            self.root = x
        
    def rotateLeft(self, node):
        if not node: return
        x = node.right
        if x == None: return
        a = x.left
        x.parent = node.parent
        if node.parent:
            if node.parent.left == node:
                node.parent.left = x
            else:
                node.parent.right = x
        x.left = node
        node.parent = x
        node.right = a
        if a:
            a.parent = node
        if self.root == node and node != None:
            self.root = x

class AVL(BST):
    def __init__(self):
        self.root = None
        self.size = 0

    def rebalance(self, x, y, z):
        #shape == True 면 linear, False 면 triangle
        v = z
        if v.left == y:	#왼쪽
            if y.left == x:
                shape = True
            elif y.right == x:
                shape = False

            if shape == True:
                self.rotateRight(z)
                return y
            else:
                self.rotateLeft(y)
                self.rotateRight(z)
                return x

        elif v.right == y:	#오른쪽
            if y.right == x:
                shape = True
            elif y.left == x:
                shape = False

            if shape == True:
                self.rotateLeft(z)
                return y
            else:
                self.rotateRight(y)
                self.rotateLeft(z)
                return x

    
    def insert(self, key):
        o = super(AVL, self).insert(key)
        v = o
        BF = 0
        zh = None
        yh = None
        if v.parent == None:
            return v
        else:
            while v != None:
                if v.left == None and v.right != None:
                    BF = self.height(v)
                elif v.right == None and v.left != None:
                    BF = 0 - self.height(v)
                elif v.left == None and v.right == None:
                    BF = 0
                elif v.left != None and v.right != None:
                    BF = self.height(v.right) - self.height(v.left)
                
                #print("노드 :", v, "BF :", BF)
                
                if BF > 1 or BF < -1:
                    #print("BF 가 2거나 -2 임!")
                    break
                yh = zh
                zh = v
                v = v.parent

            if BF > 1 or BF < -1:
                #print("그래서 x : ", yh, "y :", zh, "z :", v)
                w = self.rebalance(yh, zh, v)
                #print("W :", w)
                if w.parent == None:
                    self.root = w
        return o

    def delete(self, u):
        v = self.deleteByCopying(u)
        #print(v)
        #self.preorder(self.root)
        BF = 0
        #o = v
        while v != None:
            if v.left == None and v.right != None:
                BF = self.height(v)
            elif v.right == None and v.left != None:
                BF = 0 - self.height(v)
            elif v.left == None and v.right == None:
                BF = 0
            elif v.left != None and v.right != None:
                BF = self.height(v.right) - self.height(v.left)
                
            #print("노드 :", v, "BF :", BF)
                
            if BF > 1 or BF < -1:
                z = v
                #print("BF 가 2거나 -2 임!")
                #print("실행되고 있니?")
                if self.height(z.left) >= self.height(z.right):
                    y = z.left
                    if self.height(y.left) >= self.height(y.right):
                        x = y.left
                    else:
                        x = y.right
                else:
                    y = z.right
                    if self.height(y.left) >= self.height(y.right):
                        x = y.left
                    else:
                        x = y.right
                        
                #print("그래서 x :", x, " y :", y, " z :", z)
                v = self.rebalance(x, y, z)
                w = v
                #self.preorder(w)
                #print("W :", w)
                #print("V :", v)
                if w.parent == None:
                    self.root = w
                v = v.parent
                #print("V :", v)
            else:
                v = v.parent
        


T = AVL()
while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        v = T.insert(int(cmd[1]))
        print("+ {0} is inserted".format(v.key))
    elif cmd[0] == 'delete':
        v = T.search(int(cmd[1]))
        T.delete(v)
        print("- {0} is deleted".format(int(cmd[1])))
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

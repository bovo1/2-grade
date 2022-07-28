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
        if self.root == node and x != None:
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
        if self.root == node and x != None:
            self.root = x


class SplayTree(BST):
    def splay(self, x):
        while x != self.root:
            px = x.parent
            gpx = px.parent
            if px == self.root:
                if x == px.right:
                    self.rotateLeft(px)
                else:
                    self.rotateRight(px)
            else:
                if x == px.left and px == gpx.left:
                    self.rotateRight(px)
                    self.rotateRight(gpx)
                elif x == px.right and px == gpx.right:
                    self.rotateLeft(px)
                    self.rotateLeft(gpx)
                elif x == px.right and px == gpx.left:
                    self.rotateLeft(px)
                    self.rotateRight(gpx)
                elif x == px.left and px == gpx.right:
                    self.rotateRight(px)
                    self.rotateLeft(gpx)
        return x


    def search(self, key):
        v = super(SplayTree, self).search(key)
        if v.key != key:
            return None
        else:
            if v != None:
                self.splay(v)
            return v

    def insert(self, key):
        v = super(SplayTree, self).insert(key)
        if v.parent == None:
            return v
        else:
            self.splay(v)
            return v
    
    def delete(self, x):
        if x != self.root:
            self.splay(x) #지우려는 노드를 루트 노드로 만들고.
        Lx = x.left
        Rx = x.right
        m = x.left
 
        if Lx != None:
            while m.right != None:
                m = m.right
            self.splay(m)

            m.right = None
            m.right = Rx
            if Rx != None:
                Rx.parent = None
                Rx.parent = m
        else:
            Rx.parent = None
            self.root = Rx

T = SplayTree()
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

import sys

def Dijkstra():
	global Q, G
	while len(Q):
		u = DeleteNode()
		for v in range(len(G[u])):
			if G[u][v] != 0:
				Relax(u, v)

def DeleteNode():
	global Q
	val = Q[0]
	Q[0], Q[-1] = Q[-1], Q[0]
	Q.pop()
	heapify_down(0)
	return val

def Relax(u, v):
	global dist, G
	if dist[u] + G[u][v] < dist[v]:
		dist[v] = dist[u] + G[u][v]
		DecreaseNode(v)
	
def DecreaseNode(v):
	global Q
	for i in range(len(Q)):
		if Q[i] == v:
			heapify_up(i)
			
def heapify_up(k):
	global Q
	while k>0 and dist[Q[(k-1)//2]] > dist[Q[k]]:
		Q[k], Q[(k-1)//2] = Q[(k-1)//2], Q[k]
		k = (k-1)//2
		
def heapify_down(k):
	global Q, dist
	n = len(Q)
	l = 2*k+1
	while l < n:
		l = 2*k+1
		r = 2*k+2
		if l<n and dist[Q[l]] < dist[Q[k]]: m = l 
		else: m = k
		if r<n and dist[Q[r]] < dist[Q[m]]: m = r
		if m != k:
			Q[k], Q[m] = Q[m], Q[k]
			k = m
		else: break 


INF = sys.maxsize

n = int(input())
m = int(input())

G = [[0]*n for i in range(n)]
Q = []
connect = [0]*n

for i in range(m):
	u, v, w = [int(c) for c in input().split()]
	G[u][v] = w
	connect[u] += 1
	
for i in range(n):
	if connect[i] != 0:
		Q.append(i)

dist = [0]

for i in range(1, n):
	dist.append(INF)

Dijkstra()

for d in dist:
	if d != INF:
		print(d, end = ' ')
	else:
		print("inf", end=' ')

#사용한 힙 연산은 heapify_donw, heapify_up 을 사용하였으며, (민힙)
#힙 연산의 수행시간은 최악의 경우에 O(log n)만큼 걸린다. (delete min도 O(log n))
#각 엣지는 각각 relax와 decrease_Key를 하기 때문에 각각 O(E * log n) 시간이 걸린다.
#엣지는 n^2까지 가능하기에 O(n^2 * log n)과 같다고 볼 수 있다.
#즉 전체적인 수행시간은 O(n^2 * log n)이라고 할 수 있다.

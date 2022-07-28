from queue import PriorityQueue

def Dijkstra(V, E, src, route):
    #Min heap 생성
    pq = PriorityQueue()
    minCost = ['inf' for i in range(V)] #모든 노드에 대해 갈 수 있는 경로를 inf 로 초기화함.
    pq.put((0, src)) #힙에 수를 넣는다.
    #힙 안에 최단경로 후보가 없을 때까지 반복한다.
    while pq.qsize() > 0:
        u = pq.get()
        if minCost[u[1]] == 'inf' or minCost[u[1]] > u[0]: #방문하지 않거나 더 최단 경로가 있다면 갱신한다.
            minCost[u[1]] = u[0]
            #찾아진 노드로부터 갈 수 있는 경로 갱신.
            for i in route[u[1]]:
                pq.put((minCost[u[1]] + route[u[1]][i], i)) 
    for i in range(V):
        print(minCost[i], end=' ')
    return

V = int(input())
E = int(input())
src = 0
#경로를 저장하기 위한 리스트.
dist = [{} for i in range(V+1)]
for i in range(E):
    [u, v, cost] = list(map(int, input().split()))
    if v not in dist[u] or dist[u][v] > cost:
        dist[u][v] = cost
Dijkstra(V, E, src, dist)

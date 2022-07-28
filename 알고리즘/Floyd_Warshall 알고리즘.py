def Floyd_Warshall(G, n, m):
	n = |V|, m = |E|
	dist = 2d list with initial value ∞
	
	for each edge (u, v) of G:
		dist[u][v] = cost(u,v)
	
	for k = 0 to n-1 :
		for u = 0 to n-1 :
			for v = 0 to n-1 :
				if dist[u][v] > dist[u][k] + dist[k][v] :
					dist[u][v] = dist[u][k] + dist[k][v]
	
	return dist
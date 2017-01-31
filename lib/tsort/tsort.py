import heapq

def tsort(edges_list, vCount):
	adjs_list = {}
	indeg = {}
	for u, v in edges_list:
		if not u in adjs_list:
			adjs_list[u] = []
		adjs_list[u].append(v)
		if not v in indeg:
			indeg[v] = 0
		indeg[v] += 1
	
	pq = []
	for u in xrange(1, vCount + 1):
		if not u in indeg:
			indeg[u] = 0
		if indeg[u] == 0:
			heapq.heappush(pq, u)
	
	sortedVertices = []
	visitedCount = 0
	while len(pq) != 0:
		u = heapq.heappop(pq)
		sortedVertices.append(u)
		visitedCount += 1
		if u in adjs_list:
			for v in adjs_list[u]:
				indeg[v] -= 1
				if indeg[v] == 0:
					heapq.heappush(pq, v)

	if len(sortedVertices) == 0 or visitedCount != vCount:
		return []
	else:
		return sortedVertices
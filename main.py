from collections import deque
from heapq import heappush, heappop
import math 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    dist = {v: math.inf for v in graph}
    edges = {v: math.inf for v in graph}
    dist[source] = 0
    edges[source] = 0

    pq = [(0, 0, source)]

    while pq:
        d, e, u = heappop(pq)

        if d > dist[u] or (d == dist[u] and e > edges[u]):
            continue
        for v, w in graph[u]:
            new_d = d + w
            new_e = e + 1

            if new_d < dist[v] or (new_d == dist[v] and new_e < edges[v]):
                dist[v] = new_d
                edges[v] = new_e
                heappush(pq, (new_d, new_e, v))

    return {v: (dist[v], edges[v]) for v in graph}
    
    

    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    parents = {source: None}
    queue = deque([source])

    while queue:
        current = queue.popleft()

        for neighbor in graph.get(current, []):
            if neighbor not in parents:
                parents[neighbor] = current
                queue.append(neighbor)

    return parents

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = parents[current]

    path.reverse()
    return "".join(path[:-1])

    


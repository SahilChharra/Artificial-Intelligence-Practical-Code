from queue import Queue

graph = {
    'F': ['E', 'A'],
    'E': ['C', 'D'],
    'A': ['B', 'C'],
    'D': ['B','C'],
    'C': ['B'],
    'B': []
}

def bfs(start, goal):
    visited = set()
    queue = Queue()
    
    queue.put((start, [start], 0))
    
    while not queue.empty():
        node, path, cost = queue.get()
        
        if node == goal:
            return path, cost
        
        if node not in visited:
            visited.add(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.put((neighbor, path + [neighbor], cost + 1))
    
    return None

start = 'F'
goal = 'B'
path, cost = bfs(start, goal)
if path:
    print(f"Shortest path from {start} to {goal} is: {path}")
else:
    print
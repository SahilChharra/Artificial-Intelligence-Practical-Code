import heapq
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                x, y = divmod(state[i][j]-1, 3)
                distance += abs(x-i) + abs(y-j)
    
    print(x,y)            
    print(distance)
    return distance

def solve_8_puzzle(initial_state):
    class Node:
        def __init__(self, state, parent=None, g=0):
            self.state = state
            self.parent = parent
            self.g = g
            self.h = manhattan_distance(state)
            self.f = self.g + self.h
        
        def __lt__(self, other):
            return self.f < other.f
        
    open_set = [Node(initial_state)]
    closed_set = set()
    
    while open_set:
        current_node = heapq.heappop(open_set)
        
        if current_node.state == goal_state:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            path.reverse()
            return path
        
        for i in range(3):
            for j in range(3):
                if current_node.state[i][j] == 0:
                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        x, y = i+dx, j+dy
                        if 0 <= x < 3 and 0 <= y < 3:
                            child_state = [row[:] for row in current_node.state]
                            child_state[i][j], child_state[x][y] = child_state[x][y], child_state[i][j]
                            child_node = Node(child_state, current_node, current_node.g+1)
                            if child_node not in closed_set:
                                heapq.heappush(open_set, child_node)
        
        closed_set.add(current_node)
    
    return None

initial_state = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
path = solve_8_puzzle(initial_state)
if path:
    print("Solution found:")
    for state in path:
        print(state)
else:
    print("No solution found!")
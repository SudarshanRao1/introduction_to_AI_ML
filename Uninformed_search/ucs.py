# import heapq

# def ucs(graph, start, goal):
#     frontier = []
#     heapq.heappush(frontier, (0, start, [start]))
#     explored = set()
    
#     while frontier:
#         cost, current, path = heapq.heappop(frontier)
        
#         if current == goal:
#             return path, cost
            
#         if current in explored:
#             continue
#         explored.add(current)
        
#         for neighbour, neighbour_cost in graph[current].items():
#             if neighbour not in explored:
#                 new_cost = cost + neighbour_cost
#                 heapq.heappush(frontier, (new_cost, neighbour, path + [neighbour]))
                
#     return None, None

# graph = {
#     'A': {'B': 1, 'C': 4},
#     'B': {'A': 1, 'D': 2, 'E': 5},
#     'C': {'A': 4, 'F': 3},
#     'D': {'B': 2, 'G': 6},
#     'E': {'B': 5, 'G': 2},
#     'F': {'C': 3, 'G': 1},
#     'G': {'D': 6, 'E': 2, 'F': 1}
# }

# start_node = 'A'
# goal_node = 'G'
# path, cost = ucs(graph, start_node, goal_node)

# if path:
#     print("shortest path:", path)
#     print("total cost:", cost)
# else:
#     print("No path found.")


import heapq 

def ucs(graph ,start, goal):
    frotiner = []

    heapq.heappush(frotiner,(0,start,[start]))
    explored = set()

    while frotiner:
        cost,current,path = heapq.heappop(frotiner)

        if current == goal:
            return path , cost
        if current in explored:
            continue 
        explored.add(current)

        for neighbour , neighbour_cost in graph[current].items():
            if neighbour not in explored:
                new_cost = cost + neighbour_cost
                heapq.heappush(frotiner,(new_cost,neighbour,path + [neighbour]))

    return None , None

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2, 'G': 6},
    'E': {'B': 5, 'G': 2},
    'F': {'C': 3, 'G': 1},
    'G': {'D': 6, 'E': 2, 'F': 1}
}

start = 'A'
goal = 'G'

path , cost = ucs(graph,start,goal)

if path:
    print("the path: " ,path)
    print("the cost: ", cost)
else:
    print("not there anything")
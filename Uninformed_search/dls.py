graph = { 
    'A': ['B', 'C'], 
    'B': ['D', 'E'], 
    'C': ['F'], 
    'D': [], 
    'E': ['F'], 
    'F': [] 
}

def dls(graph,current_node,goal_node,depth_limit,path=None):
    if path is None:
        path = [current_node]

    if current_node == goal_node:
        return path

    if depth_limit <=0:
        return  None

    for neighbour in graph.get(current_node,[]):
        if neighbour not in path:
            result = dls(graph,neighbour,goal_node,depth_limit - 1,path+[neighbour])
        if result:
            return result

    return None

start_node = 'A'
goal_node = 'F'
depth_limit = 2


result = dls(graph,start_node,goal_node,depth_limit)

if result:
    print(result)
else:
    print("this is not there")
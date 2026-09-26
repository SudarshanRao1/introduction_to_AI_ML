from collections import deque

def dfs(graph, start, goal, depth_limit):

    stack = deque([(start, [start])])

    while stack:

        # Remove the last element from the stack
        current, path = stack.pop()

        # Check if goal is reached
        if current == goal:
            return path

        # Continue searching only if depth limit is not reached
        if len(path) - 1 < depth_limit:

            # Explore all neighbors
            for neighbor in graph[current]:

                # Avoid visiting nodes already in the path
                if neighbor not in path:

                    # Add neighbor and updated path to stack
                    stack.append(
                        (neighbor, path + [neighbor])
                    )

    # No path found within depth limit
    return None


def iterative_deepening_search(graph, start, goal, max_depth):
    """
    Performs Iterative Deepening Search from 'start' to 'goal'.
    """

    # Try depth limits from 0 to max_depth
    for depth in range(max_depth + 1):

        print("Searching with depth limit:", depth)

        # Perform depth-limited DFS
        result = dfs(graph, start, goal, depth)

        # If goal is found
        if result:
            return result

    # Goal not found within maximum depth
    return None


# Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


# Starting node
start_node = 'A'

# Goal node
goal_node = 'F'

# Maximum depth allowed
max_depth_limit = 3

# Perform IDDFS
path = iterative_deepening_search(
    graph,
    start_node,
    goal_node,
    max_depth_limit
)

# Display result
if path:
    print("Path found:", path)
else:
    print("No path found.")
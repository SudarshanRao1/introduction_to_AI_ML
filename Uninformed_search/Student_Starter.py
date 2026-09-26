from collections import deque

maze = [
    ['S', '.', '.'],
    ['#', '#', '.'],
    ['.', '.', 'G']
]

# Directions (Up, Down, Left, Right)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def find_start(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                return (i, j)
    return None


def bfs_maze(maze):
    start = find_start(maze)
    if start is None:
        return None

    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current, path = queue.popleft()
        x, y = current

        if maze[x][y] == 'G':
            return path

        if current in visited:
            continue
        visited.add(current)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < len(maze)
                and 0 <= ny < len(maze[0])
                and maze[nx][ny] != '#'
                and (nx, ny) not in visited
            ):
                queue.append(((nx, ny), path + [(nx, ny)]))

    return None


result = bfs_maze(maze)
print("Shortest Path:", result)

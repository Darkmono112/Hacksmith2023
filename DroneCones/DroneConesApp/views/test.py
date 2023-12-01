def getAnagramPeriod(input_str):
    last_success = len(input_str)
    count = 2
    while count <= len(input_str):
        if len(input_str) % count == 0:
            sample_size = (len(input_str) // count)
            chunks = []
            for i in range(count):
                chunk = input_str[sample_size * i: sample_size * (i + 1)]
                chunk_list = []
                for letter in chunk:
                    chunk_list.append(letter)
                chunks.append(chunk_list)

            sample = input_str[0: sample_size]
            for chunk in chunks:
                for letter in sample:
                    if letter not in chunk:
                        return last_success
                    else:
                        chunk.remove(letter)
            last_success = len(sample)
        count += 1

    return last_success

from collections import deque

def min_moves(maze, k):
    n, m = len(maze), len(maze[0])

    # Helper function to check if a cell is valid and not blocked
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m and maze[x][y] == 0

    # Possible moves: left, right, up, down
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    queue = deque([(0, 0, 0)])  # (x, y, moves)

    while queue:
        x, y, steps = queue.popleft()

        if x == n - 1 and y == m - 1:
            return steps

        for move in moves:
            for k_step in range(1, k + 1):
                dx, dy = move
                nx, ny = x + k_step * dx, y + k_step * dy

                if is_valid(nx, ny):
                    queue.append((nx, ny, steps + 1))
                    maze[nx][ny] = 1  # Mark the cell as visited to avoid revisiting

    return -1  # If no path is found

# Example usage:
maze = [
    [0, 0, 0, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 1, 0],
]
k = 2
result = min_moves(maze, k)
print(result)

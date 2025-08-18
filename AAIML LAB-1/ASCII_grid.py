# Program 2: Read an ASCII grid, find S and list all T
grid = [
    ['.', 'S', '.', 'T'],
    ['T', '.', '.', '.'],
    ['.', '.', 'T', '.']
]

start = None
tasks = []

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'S':
            start = (i, j)
        elif grid[i][j] == 'T':
            tasks.append((i, j))

print("Start Position:", start)
print("Task Cells:", tasks)

import collections
import os
import time

class ReflexAgent:
    def __init__(self, grid, max_steps=100):
        self.grid = [list(row) for row in grid]
        self.pos = self.find('A')
        self.tasks = self.find_all('T')
        self.max_steps = max_steps
        self.dimensions = (len(self.grid), len(self.grid[0]))

    def find(self, symbol):
        for r, row in enumerate(self.grid):
            try:
                c = row.index(symbol)
                return (r, c)
            except ValueError:
                continue
        return None

    def find_all(self, symbol):
        return {(r, c) for r, row in enumerate(self.grid) for c, val in enumerate(row) if val == symbol}

    def valid(self, r, c):
        rows, cols = self.dimensions
        return 0 <= r < rows and 0 <= c < cols and self.grid[r][c] != '#'

    def neighbors(self, r, c):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        return [(r + dr, c + dc) for dr, dc in directions if self.valid(r + dr, c + dc)]

    def find_path_to_nearest_task(self):
        """Finds the shortest path to the nearest uncollected task using BFS."""
        if not self.tasks:
            return None
        
        queue = collections.deque([(self.pos, [])])
        visited = {self.pos}
        
        while queue:
            current_pos, path = queue.popleft()
            
            if current_pos in self.tasks:
                return path + [current_pos]

            for neighbor in self.neighbors(*current_pos):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [current_pos]))
        return None

    def move(self):
        """Moves the agent one step along the path to the nearest task."""
        path = self.find_path_to_nearest_task()
        
        if path and len(path) > 1:
            next_pos = path[1]
            self.pos = next_pos
            if self.pos in self.tasks:
                self.tasks.remove(self.pos)
        elif path and len(path) == 1:
            
            self.tasks.remove(self.pos)
        else:
            
            pass

    def run(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Initial Grid State:")
        for row in self.grid:
            print(" ".join(row))
        time.sleep(1.5)

        for step in range(self.max_steps):
            os.system('cls' if os.name == 'nt' else 'clear')
            
            
            old_pos = self.pos
            self.move()
            
            
            self.grid[old_pos[0]][old_pos[1]] = '.'
            self.grid[self.pos[0]][self.pos[1]] = 'A'

            print(f"Grid after Step {step + 1}:")
            for row in self.grid:
                print(" ".join(row))
            print(f"Tasks remaining: {len(self.tasks)}")
            
            if not self.tasks:
                print(f"\nAll tasks collected in {step+1} steps.")
                return
            
            time.sleep(0.5)

        print("\nMax steps reached. Some tasks remain.")

grid = [
    ['#','#','#','#','#'],
    ['#','A','.','T','#'],
    ['#','.','#','.','#'],
    ['#','T','.','.','#'],
    ['#','#','#','#','#']
]

agent = ReflexAgent(grid, max_steps=100)
agent.run()
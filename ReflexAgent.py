class ReflexAgent:
    def _init_(self, grid, max_steps=20):
        self.grid = grid
        self.pos = self.find('A')
        self.tasks = self.find_all('T')
        self.max_steps = max_steps

    def find(self, symbol):
        for r, row in enumerate(self.grid):
            for c, val in enumerate(row):
                if val == symbol: return (r, c)

    def find_all(self, symbol):
        return {(r, c) for r, row in enumerate(self.grid) for c, val in enumerate(row) if val == symbol}

    def valid(self, r, c):
        return 0 <= r < len(self.grid) and 0 <= c < len(self.grid[0]) and self.grid[r][c] != '#'

    def neighbors(self, r, c):
        return [(nr, nc) for nr, nc in [(r-1,c), (r+1,c), (r,c-1), (r,c+1)] if self.valid(nr, nc)]

    def move(self):
        for nr, nc in self.neighbors(*self.pos):
            if (nr, nc) in self.tasks:
                self.tasks.remove((nr, nc))
                self.pos = (nr, nc)
                return
        nbrs = self.neighbors(*self.pos)
        if nbrs: self.pos = nbrs[0]

    def run(self):
        for step in range(self.max_steps):
            self.grid[self.pos[0]][self.pos[1]] = '.'
            self.move()
            self.grid[self.pos[0]][self.pos[1]] = 'A'
            for row in self.grid: print(" ".join(row))
            print()
            if not self.tasks:
                print(f"All tasks collected in {step+1} steps.")
                return
        print("Max steps reached. Some tasks remain.")

# Example grid
grid = [
    ['#','#','#','#','#'],
    ['#','A','.','T','#'],
    ['#','.','#','.','#'],
    ['#','T','.','.','#'],
    ['#','#','#','#','#']
]

agent = ReflexAgent(grid, max_steps=20)
agent.run()
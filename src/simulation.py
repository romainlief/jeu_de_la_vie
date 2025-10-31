import numpy as np


class GameOfLifeSimulation:
    def __init__(self, size=50, alive_prob=0.2):
        self.N = int(size)
        self.vie = float(alive_prob)
        # grille initiale aléatoire
        self._grid = np.random.choice([0, 1], (self.N, self.N), p=[1 - self.vie, self.vie])

    def step(self):
        new_grid = np.zeros((self.N, self.N), dtype=int)
        for i in range(self.N):
            for j in range(self.N):
                neighbors = self.neighbor_active_count(i, j)
                if self._grid[i, j] == 1:
                    new_grid[i, j] = 1 if (neighbors == 2 or neighbors == 3) else 0
                else:
                    new_grid[i, j] = 1 if neighbors == 3 else 0
        self._grid = new_grid
        return self._grid

    def _neighbor_active_count(self, x, y):
        count = 0
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if i == 0 and j == 0:
                    continue
                xi = (x + i) % self.N
                yj = (y + j) % self.N
                if self._grid[xi, yj] == 1:
                    count += 1
        return count
    
    def neighbor_active_count(self, x, y):
        count = 0
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if i == 0 and j == 0:
                    continue
                xi, yj = x + i, y + j
                if 0 <= xi < self.N and 0 <= yj < self.N:
                    count += self._grid[xi, yj]
        return count

    @property
    def grid(self):
        return self._grid

    @property
    def grid_size(self):
        return (self.N, self.N)

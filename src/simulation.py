import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class GameOfLifeSimulation:
    def __init__(self):
        self._grid_size = (50, 50)
        self._grid = np.random.choice([0, 1], size=self._grid_size)

    def run(self):
        while True:
            for i in range(self._grid_size[0]):
                for j in range(self._grid_size[1]):
                    pass
    
    @property
    def grid(self):
        return self._grid

    @property
    def grid_size(self):
        return self._grid_size
            
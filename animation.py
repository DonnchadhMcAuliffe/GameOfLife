# Third-party
import matplotlib.pyplot as plt
import numpy
from matplotlib import animation
from matplotlib.image import AxesImage

# Local
from game_of_life import GameOfLife

FRAMES = 500
FRAME_PER_SECOND = 10
INTERVAL = 500
LENGTH_OF_SQUARE = 40


def run_game(*args) -> AxesImage:
    """Execute one iteration of the game of life and return the new img"""
    gol.compute_new_grid()
    img.set_array(gol.grid)
    return img


gol = GameOfLife(LENGTH_OF_SQUARE)
gol.set_initial_state(numpy.random.randint(0,LENGTH_OF_SQUARE,(500,2)).tolist())
fig, ax = plt.subplots()
plt.xticks([],[])
plt.yticks([],[])
img = ax.imshow(gol.grid, cmap='binary', interpolation='nearest', animated=True)
ani = animation.FuncAnimation(fig, run_game, frames=FRAMES, interval=INTERVAL)
ani.save('game_of_life.gif', writer='imagemagick', fps=FRAME_PER_SECOND)

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Button

from simulation import GameOfLifeSimulation


def run_gui(size=50, alive_prob=0.2, interval=200):
    sim = GameOfLifeSimulation(size=size, alive_prob=alive_prob)

    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.15)
    im = ax.imshow(sim.grid, cmap="binary", interpolation="nearest")
    ax.set_title("Jeu de la Vie")
    ax.set_xticks([])
    ax.set_yticks([])

    state = {"paused": False}

    def update(frame):
        if not state["paused"]:
            grid = sim.step()
            im.set_data(grid)
        return (im,)

    ani = animation.FuncAnimation(fig, update, interval=interval, blit=True)

    axpause = plt.axes([0.7, 0.03, 0.08, 0.05])
    bpause = Button(axpause, "Pause")

    def on_pause(event):
        state["paused"] = not state["paused"]
        bpause.label.set_text("Resume" if state["paused"] else "Pause")

    bpause.on_clicked(on_pause)

    axstep = plt.axes([0.59, 0.03, 0.08, 0.05])
    bstep = Button(axstep, "Step")

    def on_step(event):
        if state["paused"]:
            grid = sim.step()
            im.set_data(grid)
            fig.canvas.draw_idle()

    bstep.on_clicked(on_step)

    axrand = plt.axes([0.44, 0.03, 0.125, 0.05])
    brand = Button(axrand, "Randomize")

    def on_randomize(event):
        sim.__init__(size=size, alive_prob=alive_prob)
        im.set_data(sim.grid)
        fig.canvas.draw_idle()

    brand.on_clicked(on_randomize)

    plt.show()

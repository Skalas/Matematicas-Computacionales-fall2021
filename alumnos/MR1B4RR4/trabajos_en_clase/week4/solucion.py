import numpy
import matplotlib.pyplot as plt


def getEvolvedCA(rule, n=30):
    ca = CA(rule, n)
    ca.start_single()
    ca.loop(n - 1)
    return ca.get_array()


class MosaicCADrawer(object):
    def __init__(self, time_steps=10):
        self.rows = 26
        self.cols = 10
        self.time_steps = time_steps

    def draw(self):
        fig, ax = plt.subplots(self.rows, self.cols, figsize=(100, 80), sharey=True)
        for row in range(self.rows):
            for col in range(self.cols):
                rule = row * self.cols + col
                if rule <= 255:
                    ca_universe = getEvolvedCA(rule, self.time_steps)

                    ax[row, col].imshow(-ca_universe)
                    ax[row, col].set_xlabel(rule)

                ax[row, col].set_xticks([])
                ax[row, col].set_yticks([])


ca_drawer = MosaicCADrawer(10)
ca_drawer.draw()

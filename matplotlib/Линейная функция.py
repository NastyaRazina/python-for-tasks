import matplotlib.pyplot as plt
import numpy as np

def lin(f1, f2, f1_label, f2_label, x_range=(-10, 10), num_points=100):
    x = np.linspace(x_range[0], x_range[1], num_points)
    y1 = f1(x)
    y2 = f2(x)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_title("Графики пересечения функций", fontsize=16)
    ax.set_xlabel("x", fontsize=14)
    ax.set_ylabel("y", fontsize=14)
    ax.grid(which="major", linewidth=1.2)
    ax.grid(which="minor", linestyle="--", color="gray", linewidth=0.5)
    ax.plot(x, y1, c="red", label=f1_label)
    ax.plot(x, y2, label=f2_label)
    ax.legend()
    ax.xaxis.set_minor_locator(plt.MultipleLocator(1))
    ax.yaxis.set_minor_locator(plt.MultipleLocator(1))
    ax.tick_params(which='major', length=10, width=2)
    ax.tick_params(which='minor', length=5, width=1)

    plt.show()
def lin1(x):
    return 6*x+11
def lin2(x):
    return -6*x+8
lin(lin1,lin2, '6x+11','-6x+8')

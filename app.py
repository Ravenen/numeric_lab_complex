import matplotlib.pyplot as plt
import numpy as np

from constants import *
from solution import runge_kutta


def display_plot(x, y, title="", x_label="", y_label="", legend=None):
    graph = plt.figure().gca()
    lines = graph.plot(x, y)
    graph.set_title(title)
    graph.set_xlabel(x_label)
    graph.set_ylabel(y_label)
    if legend:
        plt.legend(lines, legend)
    plt.show()


def get_results(interval, step, initial_values):
    intervals_quantity = int(interval / step)
    intervals = np.linspace(0, intervals_quantity * step, intervals_quantity + 1)
    values = np.zeros((intervals_quantity + 1, len(initial_values)))
    values[0] = np.array(initial_values)

    for n in range(intervals_quantity):
        values[n + 1] = runge_kutta(values[n], intervals[n], step)

    return values, intervals


if __name__ == '__main__':

    initial = [0, 0, 0]
    values_line, time_line = get_results(integration_interval, integration_step, initial)
    display_plot(time_line, values_line, "Equations", "time, s", "value", ["Uc1", "i3", "Uc2"])
    display_plot(time_line, values_line[:, 0], "Uc1", "time, s", "value, V")
    display_plot(time_line, values_line[:, 1], "i3", "time, s", "value, A")
    display_plot(time_line, values_line[:, 2], "Uc2 (U2)", "time, s", "value, V")

    currents = []
    inductance = []
    current = 0
    while current < imax + 1:
        currents.append(current)
        inductance.append(L2(current))
        current += integration_step

    display_plot(currents, inductance, "L2(i3)", "i, A", "L, H")

    input_voltage = []
    time_line = []
    time = 0
    while time < 3 * T:
        time_line.append(time)
        input_voltage.append(U1(time))
        time += integration_step

    display_plot(time_line, input_voltage, "U1(t)", "time, s", "value, V")

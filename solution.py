from equation import differential_equations_system


def runge_kutta(values, time, step):
    next_values = values[:]

    for i in range(len(values)):
        current_value = values[i]

        k1 = step * differential_equations_system[i](values, time)

        values[i] = current_value + k1 / 3
        k2 = step * differential_equations_system[i](values, time + step / 3)

        values[i] = current_value - k1 / 3 + k2
        k3 = step * differential_equations_system[i](values, time + 2 * step / 3)

        values[i] = current_value + k1 - k2 + k3
        k4 = step * differential_equations_system[i](values, time + step)

        values[i] = current_value

        next_values[i] = values[i] + (k1 + 3 * k2 + 3 * k3 + k4) / 8

    return next_values

from constants import *

differential_equations_system = [
    lambda values, time: (U1(time) - values[0] + values[1] * R3) / (C1 * (R1 + R3)),
    lambda values, time: ((R3 * (U1(time) - values[0] + values[1] * R3)) / (L2(values[1]) * (R1 + R3))) -
                         (values[1] * (R3 + R2) / L2(values[1])) - (values[2] / L2(values[1])),
    lambda values, time: values[1] / C2
]

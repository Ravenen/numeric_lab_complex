half_period = 0.02
T = 2 * half_period

integration_interval = 100 * T
integration_step = T / 400

mili = 10 ** (-3)

C1 = 54 * mili
C2 = 36 * mili
Lmax = 9.5
Lmin = 0.95
imin = 1
imax = 2
R1 = 22
R2 = 34
R3 = 45


def L2(current):
    if abs(current) <= imin:
        return Lmax
    if abs(current) >= imax:
        return Lmin

    return S3(current)


def U1(t):
    n = int(t / T)
    if n * T <= t < n * T + T / 2:
        return 10
    # if n * T + T / 2 <= t < (n + 1) * T:
    return g(t - (n * T + T / 2))


def g(x):
    return (10 / half_period) * x - 10


def S3(current):
    step = imax - imin
    b1 = (2 * (current - imin) + step) * ((imax - current) ** 2)
    b2 = (2 * (imax - current) + step) * ((current - imin) ** 2)
    b3 = (current - imin) * ((imax - current) ** 2)
    b4 = (current - imax) * ((current - imin) ** 2)
    m1 = 0
    m2 = 0
    return (b1 * Lmax + b2 * Lmin) / (step ** 3) + (b3 * m1 + b4 * m2) / (step ** 2)

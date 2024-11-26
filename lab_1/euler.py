def eulerSolver(func, x0, u0, n, h):
    res = []
    for i in range(n + 1):
        res.append(x0)
        x0 += h * func(x0, u0)
        u0 += h
    return res

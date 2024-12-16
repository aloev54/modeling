def eulerSolver(func, x0, u0, n, h):
    res = []
    for i in range(n + 1):
        res.append(x0)
        if abs(x0) > 1e154 or abs(u0) > 1e154:  # Предположим, что это предел
            print(f"OverflowWarning at step {i}: x0 = {x0}, u0 = {u0}")
            break
        x0 += h * func(x0, u0)
        u0 += h
    return res

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Данные из таблицы 1
I_values = [0.5, 1, 5, 10, 50, 200, 400, 800, 1200]
T0_values = [6730, 6790, 7150, 7270, 8010, 9185, 10010, 11140, 12010]
m_values = [0.50, 0.55, 1.7, 3, 11, 32, 40, 41, 39]

# Данные из таблицы 2
T_values = [4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000]
sigma_values = [0.031, 0.27, 2.05, 6.06, 12.0, 19.9, 29.6, 41.1, 54.1, 67.7, 81.5]

# Параметры системы
R_k = 0.25  # Ом
L_k = 187e-6  # Гн
C_k = 268e-6  # Ф
R = 0.35 / 100  # см -> м
l_e = 12 / 100  # см -> м
U_0 = 1400  # В
I_0 = 0  # А
T_w = 2000  # К

def interpolate_T_and_sigma():
    """Создание функций интерполяции для T и sigma."""
    T_interp = interp1d(I_values, T0_values, kind='linear', fill_value="extrapolate")
    m_interp = interp1d(I_values, m_values, kind='linear', fill_value="extrapolate")
    sigma_interp = interp1d(T_values, sigma_values, kind='linear', fill_value="extrapolate")
    return T_interp, m_interp, sigma_interp

def calculate_Rp(I, T_interp, m_interp, sigma_interp):
    """Расчет R_p по формуле (2)."""
    T = T_interp(I) + m_interp(I) * (T_w - T_interp(I))
    sigma = sigma_interp(T)
    integrand = lambda z: 1 / (sigma * 2 * np.pi * R)
    # Численный расчет интеграла
    Rp = np.trapz([integrand(z) for z in np.linspace(0, l_e, 100)], np.linspace(0, l_e, 100))
    return Rp

def runge_kutta_step(f, t, y, h, order):
    """Шаг метода Рунге-Кутта."""
    if order == 1:  # Метод Эйлера
        k1 = f(t, y)
        return y + h * k1
    elif order == 2:  # Метод Рунге-Кутта 2-го порядка
        k1 = f(t, y)
        k2 = f(t + h, y + h * k1)
        return y + h * (k1 + k2) / 2
    elif order == 4:  # Метод Рунге-Кутта 4-го порядка
        k1 = f(t, y)
        k2 = f(t + h / 2, y + h * k1 / 2)
        k3 = f(t + h / 2, y + h * k2 / 2)
        k4 = f(t + h, y + h * k3)
        return y + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    else:
        raise ValueError("Order must be 1, 2, or 4.")

def system_equations(t, y, T_interp, m_interp, sigma_interp):
    """Система дифференциальных уравнений."""
    I, U = y
    Rp = calculate_Rp(I, T_interp, m_interp, sigma_interp)
    dI_dt = (U - I * (R_k + Rp)) / L_k
    dU_dt = -I / C_k
    return np.array([dI_dt, dU_dt])

def solve_system(method_order=4, t_max=1e-3, dt=1e-6):
    """Численное решение системы методом Рунге-Кутта заданного порядка."""
    T_interp, m_interp, sigma_interp = interpolate_T_and_sigma()
    t_values = []
    y_values = []
    R_values = []
    T_values_list = []

    t = 0
    y = np.array([I_0, U_0])

    while t < t_max:
        Rp = calculate_Rp(y[0], T_interp, m_interp, sigma_interp)
        T = T_interp(y[0]) + m_interp(y[0]) * (T_w - T_interp(y[0]))

        t_values.append(t)
        y_values.append(y)
        R_values.append(Rp)
        T_values_list.append(T)

        y = runge_kutta_step(lambda t, y: system_equations(t, y, T_interp, m_interp, sigma_interp), t, y, dt, method_order)
        t += dt

    t_values = np.array(t_values)
    y_values = np.array(y_values)
    R_values = np.array(R_values)
    T_values_list = np.array(T_values_list)
    return t_values, y_values, R_values, T_values_list

def plot_results(t_values, y_values, R_values, T_values):
    """Построение графиков."""
    I_values = y_values[:, 0]
    U_values = y_values[:, 1]

    plt.figure(figsize=(10, 6))
    plt.plot(t_values * 1e6, I_values, label='I(t), A')
    plt.plot(t_values * 1e6, U_values, label='U(t), V')
    plt.xlabel('Time, µs')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid()
    plt.title('Графики зависимости I(t) и U(t)')
    plt.show()

    # plt.figure(figsize=(10, 6))
    # plt.plot(t_values * 1e6, R_values, label='R_p(t), Ом')
    # plt.xlabel('Time, µs')
    # plt.ylabel('R_p, Ом')
    # plt.legend()
    # plt.grid()
    # plt.title('График зависимости R_p(t)')
    # plt.show()

    # plt.figure(figsize=(10, 6))
    # plt.plot(t_values * 1e6, T_values, label='T(t), К')
    # plt.xlabel('Time, µs')
    # plt.ylabel('T, К')
    # plt.legend()
    # plt.grid()
    # plt.title('График зависимости T(t)')
    # plt.show()

if __name__ == "__main__":
    # Решение системы для метода Рунге-Кутта 4-го порядка
    t_values, y_values, R_values, T_values = solve_system(method_order=1)
    plot_results(t_values, y_values, R_values, T_values)

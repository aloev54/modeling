import math
from data import *


class Runge:
    R: float  # Радиус трубки
    l_e: float  # Расстояние между электродами лампы
    L_k: float  # Индуктивность
    C_k: float  # Емкость конденсатора
    R_k: float  # Сопротивление
    U_co: float  # Напряжение на кодненсаторе в нач. момент времени
    I_o: float  # Сила тока в нач. момент времени
    T_w: float  # Температура
    I_max: float  # Максимальный ток
    P_t: float  # Длительность импульса

    STEP = 1/30
    H = 1e-6

    def __init__(self):
        self.R = 0.35  # см
        self.l_e = 12  # см
        self.L_k = 187e-6  # Гн
        self.C_k = 268e-6  # Ф
        self.R_k = 0.25  # Ом
        self.U_co = 1400  # В
        self.I_o = 0.3  # A
        self.T_w = 2000  # K
        self.I_max = 800  # A
        self.P_t = 600e-6  # c

        self.T_0 = t_0  # Массив Т0 для интерполяции
        self.I = i  # Массив I для интерполяции
        self.M = m  # Массив m для интерполяции
        self.Sigma = sigma  # Массив sigma для интерполяции
        self.T = t  # Массив Т для интерполяции

        self.i_res = []
        self.u_res = []
        self.tau_res = []
        self.r_res = []

    def dI_dt(self, u, i, R_p):
        return (u-(self.R_k+R_p)*i)/self.L_k

    def dU_dt(self, i):
        return -i/self.C_k

    def interpolate(self, arr1, arr2, value):
        for j in range(len(arr1) - 1):
            if arr1[j] <= value <= arr1[j + 1]:
                return arr2[j] + (arr2[j + 1] - arr2[j]) * (value - arr1[j]) / (arr1[j + 1] - arr1[j])
        return arr2[-1]

    def R_p(self, i):
        sigma_sum = sum(
            self.interpolate(self.T, self.Sigma,
                             self.interpolate(self.I, self.T_0, i))
            for _ in range(1/self.STEP)
        )
        return self.l_e/(2*math.pi*self.R**2*sigma_sum)
    
    def eulerSolver(self, tau=0, tau_max=0.001):
        self.i_res.clear()
        self.u_res.clear()
        self.tau_res.clear()

        i_0, u_0, tau_0 = self.I_o, self.U_co, tau

        while tau_0<tau_max:
            r_0 = self.R_p(i_0)
            di = self.dI_dt(u_0,i_0,r_0)
            du = self.dU_dt(i_0)
            tau_0 += self.H
            u_0 += du * self.H
            i_0 += di * self.H
            self.i_res.append(i_0)
            self.u_res.append(u_0)
            self.tau_res.append(tau_0)
            self.r_res.append(r_0)

    def RungeSolver2(self,tau=0,tau_max=0.01,alpha =0.5):
        self.i_res.clear()
        self.u_res.clear()
        self.tau_res.clear()

        i_0, u_0, tau_0 = self.I_o, self.U_co, tau

        while tau_0<tau_max:
            r_0 = self.R_p(i_0)
            k1 = self.H * self.dI_dt(u_0,i_0,r_0)
            q1 = self.H * self.dU_dt(i_0)
            k2 = self.H * self.dI_dt(u_0 + self.H*alpha,i_0 + k1*alpha,r_0 + self.H*alpha)
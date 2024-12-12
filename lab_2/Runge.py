class Runge:
    R: float #Радиус трубки
    l_e: float #Расстояние между электродами лампы
    L_k: float #Индуктивность
    C_k: float #Емкость конденсатора
    R_k: float #Сопротивление
    U_co: float #Напряжение на кодненсаторе в нач. момент времени
    I_o: float #Сила тока в нач. момент времени
    T_w: float #Температура
    I_max: float #Максимальный ток
    P_t: float #Длительность импульса

    def __init__(self):
        self.R = 0.35 #см
        self.l_e = 12 #см
        self.L_k = 187e-6 #Гн
        self.C_k = 268e-6 #Ф
        self.R_k = 0.25 #Ом
        self.U_co = 1400 #В
        self.I_o = 0.3 #A
        self.T_w = 2000 #K
        self.I_max = 800 #A
        self.P_t = 600e-6 #c
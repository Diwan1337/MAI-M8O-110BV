import matplotlib.pyplot as plt

import numpy as np

# параметры ракеты и взлёта

time = 85  # время работы первой ступени в сек
m0 = 431 * 10 ** 3  # начальная масса корабля в кг
Ft = 6781.2 * 10 ** 3  # тяга ускорителя 1-ой ступени в кН
k = 2470.6  # скорость расхода топлива в кг/с
b = -0.001  # изменение угла движения ракеты рад/с
cf = 0.2  # коэффициент сопротивления
S = 133.01  # площадь лобового сопротивления

# константы
e = 2.72
shag = 0.1  # шаг (по желанию изменяемая переменная)
Ang0 = np.pi / 2
Ang1 = Ang0 + time * b
G = 9.81
M_A = 0.29
R = 8.31
T = 300
P_0 = 10 ** 5
GAZ_P = M_A / (R * T)

x_values = [0]
y_values = [0]
vx_values = [0]
vy_values = [0]
ax_values = [0]
ay_values = [-9.81]

x = 0
y = 0
vx = 0
vy = 0
ax = 0
ay = 0

for i in range(int(time // shag)):  # рассчитываем n сек
    t = i * shag
    rho = (GAZ_P * P_0) * (e ** (-G * y * GAZ_P))
    f_cx = cf * S * (rho * (vx_values[-1] ** 2) * 0.5)
    f_cy = cf * S * (rho * (vy_values[-1] ** 2) * 0.5)
    ax = ((Ft) * np.cos(Ang0 + b * t) - f_cx)/(m0 - k * t)
    ay = ((Ft) * np.sin(Ang0 + b * t) - f_cy)/(m0 - k * t) - G
    vx = vx_values[-1] + ax * shag
    vy = vy_values[-1] + ay * shag
    x = x_values[-1] + vx * shag
    y = y_values[-1] + vy * shag
    ax_values.append(ax)
    ay_values.append(ay)
    vx_values.append(vx)
    vy_values.append(vy)
    x_values.append(x)
    y_values.append(y)


velocity = [((vx_values[i]) ** 2 + vy_values[i] ** 2)
            ** 0.5 for i in range(len(vx_values))]
# print([((vx_values[::10][i]) ** 2 + vy_values[::10][i] ** 2) ** 0.5 for i in range(time)])
# print(y_values[::100])
# plt.plot(range(0, time), vx_values[::int(shag ** -1)])
# plt.xlabel("время, с")
# plt.ylabel("высота, м")
# plt.plot(range(0, time), y_values[::int(shag ** -1)])
plt.xlabel("время, с")
plt.ylabel("скорость, м/с")
plt.plot(range(0, time), velocity[::int(shag ** -1)])
plt.show()

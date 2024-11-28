import matplotlib.pyplot as plt
import numpy as np

# Параметры ракеты и взлёта
time = 130      # Время работы первой ступени (сек)
m0 = 750000     # Начальная масса корабля (кг)
Ft = 9400000    # Тяга первой ступени (Н)
k = 3400        # Скорость расхода топлива (кг/с)
b = -0.0005     # Изменение угла движения ракеты (рад/с)
cf = 0.32       # Коэффициент сопротивления
S = 14.89       # Площадь лобового сопротивления (м²)

# Константы
e = 2.72
shag = 0.1      # Шаг расчета (сек)
Ang0 = np.pi / 2  # Стартовый угол (90 градусов)
Ang1 = Ang0 + time * b
G = 9.81        # Ускорение свободного падения (м/с²)
M_A = 0.029     # Молекулярная масса воздуха (кг/моль)
R = 8.31        # Газовая постоянная (Дж/(моль·К))
T = 300         # Температура (К)
P_0 = 10 ** 5   # Атмосферное давление (Па)
GAZ_P = M_A / (R * T)

# Переменные
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

# Расчет траектории
for i in range(int(time // shag)):  # Рассчитываем траекторию на n секунд
    t = i * shag
    rho = (GAZ_P * P_0) * (e ** (-G * y * GAZ_P))  # Плотность атмосферы
    f_cx = cf * S * (rho * (vx_values[-1] ** 2) * 0.5)  # Сопротивление по X
    f_cy = cf * S * (rho * (vy_values[-1] ** 2) * 0.5)  # Сопротивление по Y
    ax = ((Ft) * np.cos(Ang0 + b * t) - f_cx) / (m0 - k * t)
    ay = ((Ft) * np.sin(Ang0 + b * t) - f_cy) / (m0 - k * t) - G
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

# Рассчитываем скорость
velocity = [((vx_values[i]) ** 2 + vy_values[i] ** 2) ** 0.5 for i in range(len(vx_values))]

# Построение графика скорости
plt.figure(figsize=(10, 5))
plt.xlabel("Время, с")
plt.ylabel("Скорость, м/с")
plt.title("График скорости ракеты Протон-К")
plt.plot(range(0, int(time)), velocity[::int(shag ** -1)], label="Скорость")
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

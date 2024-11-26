import matplotlib.pyplot as plt  # библиотека для рисования графиков
import krpc  # библиотека для подключения к KSP и сбора данных
import time

# Подключение к игре
conn = krpc.connect(name='Speed vs Time Graph')
vessel = conn.space_center.active_vessel
orbit_frame = vessel.orbit.body.reference_frame

# Переменные для графика
speeds = []  # Скорости
times = []  # Время

# Сбор данных
print("Сбор данных о скорости...")
start_time = vessel.met  # Стартовое время
while True:
    current_speed = vessel.flight(orbit_frame).speed  # Скорость в м/с
    current_time = vessel.met - start_time  # Время с момента запуска

    speeds.append(current_speed)
    times.append(current_time)

    print(f"Время: {current_time:.2f} с | Скорость: {current_speed:.2f} м/с")

    # Условие выхода из цикла
    if current_speed > 1000:  # Например, прекращаем сбор данных при достижении 1000 м/с
        break

    time.sleep(0.1)  # Интервал между замерами

# Построение графика
print("Рисуем график...")
plt.figure(figsize=(10, 5))
plt.plot(times, speeds, label="Скорость от времени")
plt.xlabel("Время (с)")
plt.ylabel("Скорость (м/с)")
plt.title("График изменения скорости ракеты")
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

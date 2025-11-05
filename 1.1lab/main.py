# Задание из банка задач ЕГЭ [https://math-ege.sdamgia.ru/problem?id=77422]
# Найти наибольшее значение функции y = x^3 - 3x + 4 на отрезке [-2; 0]
import numpy as np
# Определяем значения x на интервале [-2, 0]
x=np.linspace(-2, 0, 1000)
y=x**3-3*x+4
max_y=max(y_values)
print('Максимальное значение:', max_y)

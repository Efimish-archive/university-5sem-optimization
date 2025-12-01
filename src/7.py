import math
import numpy as np
import sympy as sp

x = sp.Symbol('x')
f = sp.sqrt(x**2 + 5) / (2*x + 3)
f = sp.lambdify(x, f, 'math')

def golden_ratio(a, b, epsilon=1e-3):
  "Метод золотого сечения"
  alpha = a + (3 - math.sqrt(5)) / 2 * (b-a)
  beta = a + (math.sqrt(5) - 1) / 2 * (b-a)
  f_alpha = f(alpha)
  f_beta = f(beta)

  while abs(b - a) > epsilon:
    # Проверяем тройку (a, x_left, x_right)
    if a < alpha < beta:
      if f(a) >= f_alpha <= f_beta:
        return a, alpha, beta
    # Проверяем тройку (x_left, x_right, b)
    if alpha < beta < b:
      if f_alpha >= f_beta <= f(b):
        return alpha, beta, b
    # Делаем шаг золотого сечения
    if f_alpha <= f_beta:
      # <--- b
      b = beta
      beta = alpha
      alpha = a + b - alpha
    else:
      # a --->
      a = alpha
      alpha = beta
      beta = a + b - beta
    f_alpha = f(alpha)
    f_beta = f(beta)
  print("На заданном отрезке функция монотонна, пораболу найти нельзя")
  exit()

def parabolic(a, b, epsilon=1e-3):
  "Метод парабол"
  x1, x2, x3 = np.linspace(a, b, 5)[1:-1]
  f1, f2, f3 = f(x1), f(x2), f(x3)
  k = 1

  if not (x1 < x2 < x3 and f1 >= f2 <= f3):
    print('Неравенство 2.9 не выполнитось, используем метод золотого сечения')
    # Снизим точность
    x1, x2, x3 = golden_ratio(a, b, epsilon*10)

  while True:
    f1, f2, f3 = f(x1), f(x2), f(x3)
    print(f"--- Итерация {k} ---")
    print(f"x1 = {x1}, x2 = {x2}, x3 = {x3}")
    print(f"f1 = {f1}, f2 = {f2}, f3 = {f3}")

    # Шаг 2
    a0 = f1
    a1 = (f2 - f1)/(x2 - x1)
    a2 = 1/(x3 - x2) * ((f3 - f1)/(x3 - x1) - (f2 - f1)/(x2 - x1))
    x_ = 0.5 * (x1 + x2 - (a1/a2))

    # Шаг 3
    if k > 1:
      d = abs(previous_x_ - x_)
      if d <= epsilon:
        print(f"Точка минимума - {x_}")
        print(f"Значение функции в этой точке - {f(x_)}")
        return
      # Лимит в 1000 итераций
      if k > 1000:
        print("Количество итераций = 1000, останавливаем поиск")
        print(f"Точка минимума - {x_}")
        print(f"Значение функции в этой точке - {f(x_)}")
        return

    # Шаг 4
    fx_ = f(x_)
    print(f"x_ = {x_}, f(x_) = {fx_}")
    if x2 <= x_ and x_ <= x3 and fx_ <= f2:
      x1 = x2
      x2 = x_
      print("x2 <= x_ <= x3, f(x_) <= f2", "x1 = x2, x2 = x_", sep="\n")
    elif x2 <= x_ and x_ <= x3 and fx_ > f2:
      x3 = x_
      print("x2 <= x_ <= x3, f(x_) > f2", "x3 = x_", sep="\n")
    elif x1 <= x_ and x_ <= x2 and fx_ <= f2:
      x3 = x2
      x2 = x_
      print("x1 <= x_ <= x2, f(x_) <= f2", "x3 = x2, x2 = x_", sep="\n")
    elif x1 <= x_ and x_ <= x2 and fx_ > f2:
      x1 = x_
      print("x1 <= x_ <= x2, f(x_) > f2", "x1 = x_", sep="\n")

    k += 1
    previous_x_ = x_

a = 2
b = 4
epsilon = 1e-3

parabolic(a, b, epsilon)

import math
import numpy as np
import sympy as sp

x = sp.Symbol('x')
f = sp.sqrt(x**2 + 5) / (2*x + 3)
f = sp.lambdify(x, f, 'math')

def golden_ratio(a, b, epsilon=1e-3):
  "Метод золотого сечения"
  a0, b0 = a, b
  alpha = a0 + (3 - math.sqrt(5)) / 2 * (b0-a0)
  beta = a0 + (math.sqrt(5) - 1) / 2 * (b0-a0)
  k = 1
  while True:
    if f(alpha) <= f(beta):
      a_current = a0
      b_current = beta
      alpha_next = a_current + b_current - alpha
      beta_next = alpha
    else:
      a_current = alpha
      b_current = b0
      alpha_next = beta
      beta_next = a_current + b_current - beta
    l = b_current - a_current
    if l <= epsilon:
      return a_current, (a_current + b_current)/2, b_current
    k += 1
    a0 = a_current
    b0 = b_current
    alpha = alpha_next
    beta = beta_next

def golden_ratio_step(a, b):
  "Один шаг методом золотого сечения"
  alpha = a + (3 - math.sqrt(5)) / 2 * (b-a)
  beta = a + (math.sqrt(5) - 1) / 2 * (b-a)
  if f(alpha) <= f(beta):
    b = beta
  else:
    a = alpha
  return a, (a+b)/2, b

def parabolic(a, b, epsilon=1e-3):
  "Метод парабол"
  x1, x2, x3 = np.linspace(a, b, 5)[1:-1]
  f1, f2, f3 = f(x1), f(x2), f(x3)
  k = 1

  while not (x1 < x2 < x3 and f1 >= f2 <= f3) :
    print('Неравенство 2.9 не выполнитось, делаем итерацию метода золотого сечения')
    x1, x2, x3 = golden_ratio_step(x1, x3)
    f1, f2, f3 = f(x1), f(x2), f(x3)

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
        print(f"Значение функции в этой точке - {fx_}")
        return
      # Лимит в 1000 итераций
      if k > 1000:
        print("Количество итераций = 1000, останавливаем поиск")
        print(f"Точка минимума - {x_}")
        print(f"Значение функции в этой точке - {fx_}")
        return

    # Шаг 4
    fx_ = f(x_)
    print(f"x_ = {x_}, f(x_) = {fx_}")
    if x2 <= x_ and x_ <= x3 and fx_ <= f2:
      x1 = x2
      x2 = x_
    elif x2 <= x_ and x_ <= x3 and fx_ > f2:
      x3 = x_
    elif x1 <= x_ and x_ <= x2 and fx_ <= f2:
      x3 = x2
      x2 = x_
    elif x1 <= x_ and x_ <= x2 and fx_ > f2:
      x1 = x_

    k += 1
    previous_x_ = x_

a = 2
b = 4
epsilon = 1e-3

parabolic(a, b, epsilon)

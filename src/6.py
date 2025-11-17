import math
import sympy as sp
import numpy as np

def f(x):
  return -1*math.sqrt(20*x - x**2) + 0.01*math.sin(x)

def f_(value):
  "Производная f'(x)"
  x = sp.symbols('x')
  expr = -1*sp.sqrt(20*x - x**2) + 0.01*sp.sin(x)
  expr = sp.diff(expr)
  expr = expr.subs(x, value)
  return expr.evalf()

def lipschitz(a, b, n):
  "Константа Липшица"
  points = np.linspace(a, b, n)
  derivatives = [f_(x) for x in points]
  return float(np.max(np.abs(derivatives)))

a = 9  # a > 0
b = 10 # b < 20
epsilon = 0.015
n = math.ceil((b - a) / epsilon)
L = lipschitz(a, b, n)

print(f"a={a}, b={b}, epsilon={epsilon}, n={n}, L={L}")

def bruteforce(a, b, n):
  "Метод равномерного перебора"
  h = 2*epsilon / L
  print(f"h={h}")
  points = np.linspace(a+h/2, b-h/2, n)
  values = [f(i) for i in points]
  min_value = min(values)
  min_index = values.index(min_value)
  return points[min_index].item(), min_value

def broken_lines(a, b, epsilon, L):
  "Метод ломаных"
  pairs: list[tuple[float, float]] = []

  x0 = (1/(2*L)) * (f(a) - f(b) + L*(a+b))
  y0 = (1/2) * (f(a) + f(b) + L*(a-b))
  pairs.append((x0, y0))

  iterations = 1
  while iterations <= 1000:
    print()
    print(f"Итерация {iterations}:")
    min_index = min(range(len(pairs)), key=lambda i: pairs[i][1])
    x_start, p_start = pairs.pop(min_index)
    print(f"Выбранная пара: ({x_start}, {p_start})")

    f_start = f(x_start)
    delta = (1/(2*L)) * (f_start - p_start)
    x1 = x_start - delta
    x2 = x_start + delta
    p_new = (1/2) * (f_start + p_start)

    if 2*L*delta <= epsilon:
      print("Окончание поиска")
      return x_start, f_start

    pairs.append((x1, p_new))
    pairs.append((x2, p_new))
    print(f'Множество пар: {pairs}')

    iterations += 1
  print("Достигнуто максимальное количество итераций")
  return x_start, f(x_start)


print("Метод равномерного перебора:", bruteforce(a, b, n))
print("Метод ломаных:", broken_lines(a, b, epsilon, L))

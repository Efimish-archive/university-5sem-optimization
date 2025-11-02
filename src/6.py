import math
import sympy
import numpy as np

def f(x):
  return -1*math.sqrt(20*x - x**2) + 0.01*math.sin(x)

def f_(value):
  "Производная f'(x)"
  x = sympy.symbols('x')
  expr = -1*sympy.sqrt(20*x - x**2) + 0.01*sympy.sin(x)
  expr = sympy.diff(expr)
  expr = expr.subs(x, value)
  return expr.evalf()

def lipschitz(a, b, n):
  "Константа Липшица"
  points = np.linspace(a, b, n)
  derivatives = [f_(x) for x in points]
  return np.max(np.abs(derivatives))

a = 9
b = 11
epsilon = 0.015
n = math.ceil((b - a) / epsilon)
L = lipschitz(a, b, n)

def bruteforce(a, b, epsilon, n):
  "Метод равномерного перебора"
  points = [a + i*epsilon for i in range(n)]
  values = [f(i) for i in points]
  min_value = min(values)
  min_index = values.index(min_value)
  return points[min_index]

def broken_lines(a, b, epsilon, n, L):
  "Метод ломаных"
  # Шаг 2
  x0 = (1/(2*L)) * (f(a) - f(b) + L*(a+b))
  y0 = (1/2) * (f(a) + f(b) + L*(a-b))
  phi_min = y0
  # Шаг 3
  while True:
    delta = (1/(2*L)) * (f(x0) - phi_min)
    # Шаг 4
    if 2*L*delta < epsilon:
      return x0 # -> x_min
    # Шаг 5
    x1L = x0 - delta
    x1R = x0 + delta
    phi = (1/2) * (f(x0) + phi_min)
    # Шаг 6
    if f(x1L) < f(x1R):
      x0 = x1L
    else:
      x0 = x1R
    phi_min = phi

print(bruteforce(a, b, epsilon, n))
print(broken_lines(a, b, epsilon, n, L))

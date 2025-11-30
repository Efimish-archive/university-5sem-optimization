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
  while True:
    if f(alpha) <= f(beta):
      b = beta
      alpha_next = a + b - alpha
      beta_next = alpha
    else:
      a = alpha
      alpha_next = beta
      beta_next = a + b - beta
    if b - a <= epsilon:
      return a, (a+b)/2, b
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

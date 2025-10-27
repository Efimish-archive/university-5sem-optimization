import math
import sympy

def f(x):
  return math.exp(-2*x) + (x**2)/2

def f_(value):
  "Производная f'(x)"
  x = sympy.symbols('x')
  expr = sympy.exp(-2*x) + (x**2)/2
  expr = sympy.diff(expr)
  expr = expr.subs(x, value)
  return expr.evalf()

def secant(a, b, epsilon=1e-3):
  "Метод секущих"
  steps = 0
  x0 = a
  x1 = b
  while abs(f_(x1)) > epsilon:
    x = x0 - (x1 - x0) * f_(x0) / (f_(x1) - f_(x0))
    if x < a or x > b:
      fa, fb = f(a), f(b)
      if fa <= fb:
        xmin, fmin = a, fa
      else:
        xmin, fmin = b, fb
      return xmin, fmin, steps
    x0, x1 = x1, x
    steps += 1
  xmin = x1
  fmin = f(x1)
  return xmin, fmin, steps

xmin, fmin, steps = secant(0, 2)
print(f"x = {xmin}")
print(f"f(x) = {fmin}")
print(f"Кол-во шагов = {steps}")

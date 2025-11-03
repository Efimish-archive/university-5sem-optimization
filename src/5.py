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

def f__(value):
  "Производная второго порядка f''(x)"
  x = sympy.symbols('x')
  expr = sympy.exp(-2*x) + (x**2)/2
  expr = sympy.diff(expr)
  expr = sympy.diff(expr)
  expr = expr.subs(x, value)
  return expr.evalf()

def newton_raphson(a, b, epsilon=1e-3):
  "Метод Ньютона-Рафсона"
  iterations = 0
  max_iterations = 200
  # Начальное приближение - середина интервала
  x_current = (a + b) / 2
  while True:
    fx = f(x_current)
    f_x = f_(x_current)
    f__x = f__(x_current)

    x_tilda = x_current - f_x/f__x
    tau = (f_x)**2 / ((f_x)**2 + (f_(x_tilda))**2)
    print(f"x_tilda = {x_tilda}, tau = {tau}")

    # Текущее состояние
    print(f"{iterations:>2}) {x_current:<15.8f} {fx:<15.8f} {f_x:<15.8f}")

    # Проверка критерия остановки: |f'(x)| < epsilon
    if abs(f_x) <= epsilon:
      print(f"Сходимость достигнута: |f'(x)| = {abs(f_x)} < {epsilon}")
      break

    # Проверка на нулевую вторую производную
    if abs(f__x) < 1e-12:
      print("Ошибка: Метод непременим, f''(x) близка к 0")
      break

    x_next = x_current - tau * (f_x / f__x)

    x_current = x_next
    iterations += 1
    if iterations > max_iterations:
      print("Достигнуто максимальное количество итераций")
      break
  print(f"Результат: x* = {x_current}, f(x*) = {f(x_current)}")
  print(f"Итераций: {iterations}")

newton_raphson(0, 2)

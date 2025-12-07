import numpy as np
import sympy as sp

x1, x2, x3 = sp.symbols('x1,x2,x3')

f = 3*x1**2 + 5*x2**2 + 4*x3**2 + 2*x1*x2 - x1*x3 - x2*x3 + 7*x1 + x3

f_x1 = sp.diff(f, x1)
f_x1_x1 = sp.diff(f_x1, x1)
f_x1_x2 = sp.diff(f_x1, x2)
f_x1_x3 = sp.diff(f_x1, x3)

f_x2 = sp.diff(f, x2)
f_x2_x1 = sp.diff(f_x2, x1)
f_x2_x2 = sp.diff(f_x2, x2)
f_x2_x3 = sp.diff(f_x2, x3)

f_x3 = sp.diff(f, x3)
f_x3_x1 = sp.diff(f_x3, x1)
f_x3_x2 = sp.diff(f_x3, x2)
f_x3_x3 = sp.diff(f_x3, x3)

f = sp.lambdify([x1, x2, x3], f, 'math')
f_x1 = sp.lambdify([x1, x2, x3], f_x1, 'math')
f_x2 = sp.lambdify([x1, x2, x3], f_x2, 'math')
f_x3 = sp.lambdify([x1, x2, x3], f_x3, 'math')

# ------------------------>

epsilon = 0.01
N = 10
# Матрица вторых производных Гессе (Hessian).
H = np.array([
  [f_x1_x1, f_x1_x2, f_x1_x3],
  [f_x2_x1, f_x2_x2, f_x2_x3],
  [f_x3_x1, f_x3_x2, f_x3_x3],
])


def steepest_gradient_descent(a, b):
  "Метод наискорейшего градиентного спуска"
  x0 = (a+b)/2
  k = 0
  funcs = [f_x1, f_x2, f_x3]
  tk = 1
  values = [i(x0, x0, x0) * tk for i in funcs]

steepest_gradient_descent(-5, 5)

# Шаг = tk

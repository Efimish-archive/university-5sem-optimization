import sympy as sp
import numpy as np

x1, x2 = sp.symbols('x1,x2')
f = (x1 - 2*x2)**2 + (x2 - 3)**2

grad_f_sym = sp.Matrix([sp.diff(f, x1), sp.diff(f, x2)])
hessian_sym = sp.hessian(f, [x1, x2])

grad_f_numeric = sp.lambdify([x1, x2], grad_f_sym, 'numpy')
hessian_numeric = sp.lambdify([x1, x2], hessian_sym, 'numpy')

x = np.array([-7, 7])
eps = 0.2

def newton(x, eps):
  "Метод Ньютона"
  i = 0
  while True:
    g = grad_f_numeric(x[0], x[1])
    h = hessian_numeric(x[0], x[1])

    g = np.array(g).flatten()
    p = np.linalg.solve(h, -g)

    if np.linalg.norm(p) <= eps:
      break

    x = x + p
    i += 1

  eigenvalues = np.linalg.eigvals(h)

  if all(eig > 0 for eig in eigenvalues):
    print(f'Нашли точку минимума x = {x[0].item(),x[1].item()} ')
  elif all(eig < 0 for eig in eigenvalues):
    print(f'Нашли точку максимума x = {x[0].item(),x[1].item()}')
  else:
    print(f'Нашли селовую точку x = {x[0].item(),x[1].item()}')

  print(f"{i}) x = ({x[0]}, {x[1]})")

newton(x, eps)

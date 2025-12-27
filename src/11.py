import sympy as sp
import numpy as np

x1, x2 = sp.symbols('x1,x2')
f = (x1 - 2*x2)**2 + (x2 - 3)**2

gradient = sp.Matrix([sp.diff(f, x1), sp.diff(f, x2)])
hessian = sp.hessian(f, [x1, x2])

gradient = sp.lambdify([x1, x2], gradient)
hessian = sp.lambdify([x1, x2], hessian)

x = np.array([-7, 7])
eps = 0.2

def newton(x, eps):
  "Метод Ньютона"
  i = 0
  # for _ in range(1000):
  while True:
    print(f'{i}) x = {x[0].item(),x[1].item()}')
    g = gradient(x[0], x[1])
    h = hessian(x[0], x[1])

    g = np.array(g).flatten()
    p = np.linalg.solve(h, -g)
    # print(f'h = {h}, g = {g}, p = {p}, norm = {np.linalg.norm(p)}')

    if np.linalg.norm(p) <= eps:
      break

    x = x + p
    i += 1

  # Вычисляем собственные значения
  eigenvalues = np.linalg.eigvals(h)

  if all(eig > 0 for eig in eigenvalues):
    print(f'Нашли точку минимума x = {x[0].item(),x[1].item()}')
  elif all(eig < 0 for eig in eigenvalues):
    print(f'Нашли точку максимума x = {x[0].item(),x[1].item()}')
  else:
    print(f'Нашли седловую точку x = {x[0].item(),x[1].item()}')

# Начальная точка X^0 = (-7, -7)
newton(x, eps)
# Теоретические рассчеты: f(6, 3) = 0

import numpy as np
import sympy as sp

x1, x2, x3 = sp.symbols('x1,x2,x3')

# функция квадратичная
f = 3*x1**2 + 5*x2**2 + 4*x3**2 + 2*x1*x2 - x1*x3 - x2*x3 + 7*x1 + x3
gradient = sp.Matrix([sp.diff(f, x1), sp.diff(f, x2), sp.diff(f, x3)])
hessian = sp.hessian(f, (x1, x2, x3))

print(f)
print(gradient)
print(hessian)

f = sp.lambdify((x1, x2, x3), f)
gradient = sp.lambdify((x1, x2, x3), gradient)
hessian = np.array(hessian, dtype=float)

def get_steepest_alpha(g, A):
  p = -g
  return -np.dot(g, p) / np.dot(p, np.dot(A, p))

def steepest_gradient_descent(X, epsilon = 0.01):
  "Метод наискорейшего градиентного спуска"
  for iteration in range(10):
    current_f = f(*X)
    current_g = gradient(*X).flatten()

    print(f"Итерация {iteration+1}: X={X}, f(X)={current_f}, g(X)={current_g}")

    if np.linalg.norm(current_g) <= epsilon:
      print(f"Сходимость достигнута!")
      break

    alpha = get_steepest_alpha(current_g, hessian)

    X -= alpha * current_g
  else:
    print("Достигнуто максимальное количество итераций")
  print(f"Точка минимума: {X}")
  print(f"Значение функции: {current_f:.6f}")
  eigenvalues = np.linalg.eigvals(hessian)
  min_l, max_l = np.min(eigenvalues), np.max(eigenvalues)
  print(f"Собственные значения: min={min_l:.2f}, max={max_l:.2f}, отношение={min_l/max_l:.4f}")

X = np.array([10, 10, 10], dtype=float)
steepest_gradient_descent(X)

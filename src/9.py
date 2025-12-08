import math
import sympy as sp

x1, x2 = sp.symbols('x1,x2')
f = (x1 - 2*x2)**2 + (x2 - 3)**2
f = sp.lambdify((x1, x2), f)

def golden_ratio(f, a=-20.0, b=20.0, epsilon=1e-3):
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
      return (a + b) / 2
    alpha = alpha_next
    beta = beta_next

def vector_norm(v1, v2):
  "Норма вектора (евклидова)"
  return math.sqrt((v1[0] - v2[0])**2 + (v1[1] - v2[1])**2)

def cyclic_coordinate_descent(x0, epsilon=0.2):
  "Метод циклического покоординатного спуска"
  vectors = [[1, 0], [0, 1]]
  iterations = 0
  for _ in range(1000):
    x0_prev = x0.copy()
    for v in vectors:
      # phi(alpha) = f(xy + alpha * e_i)
      def phi(alpha):
        new_x1 = x0[0] + alpha * v[0]
        new_x2 = x0[1] + alpha * v[1]
        return f(new_x1, new_x2)

      # Находим оптимальный шаг alpha
      alpha = golden_ratio(phi, epsilon=epsilon)
      x0[0] += alpha * v[0]
      x0[1] += alpha * v[1]

    iterations += 1
    if vector_norm(x0, x0_prev) <= epsilon:
      print(f"Сходимость достигнута за {iterations} итераций.")
      break
  else:
    print(f"Достигнуто максимальное число итераций.")

  print(f"Минимум найден в точке: x1 = {x0[0]:.6f}, x2 = {x0[1]:.6f}")
  print(f"Значение функции: f = {f(x0[0], x0[1]):.6f}")


# Начальная точка X^0 = (-7, -7)
cyclic_coordinate_descent([-7.0, -7.0])
# Теоретические рассчеты: f(6, 3) = 0

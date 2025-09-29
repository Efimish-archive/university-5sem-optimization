from tabulate import tabulate

def f(x):
  return (2 * x * (2 * x + 3)) / (x**2 + 4 * x + 5)

def print_table(left, alpha, beta, right):
  print(tabulate([
    ['x', left, alpha, beta, right],
    ['f(x)', f(left), f(alpha), f(beta), f(right)]
  ], headers = ['Левая граница', 'Альфа', 'Бета', 'Правая граница'], tablefmt = 'fancy_grid', floatfmt=".9f"))

def dihotomy(left, right, epsilon=1e-3):
  i = 1
  sigma = epsilon / 4
  while right - left > epsilon:
    middle = (left + right) / 2
    alpha = middle - sigma
    beta = middle + sigma

    print(f'Шаг {i})')
    print_table(left, alpha, beta, right)

    if f(alpha) <= f(beta):
      right = beta
      print('<--- Двигаем правую границу в бета <---')
    else:
      print('---> Двигаем левую границу в альфа --->')
      left = alpha

    middle = (left + right) / 2
    alpha = middle - sigma
    beta = middle + sigma
    print_table(left, alpha, beta, right)
    print()
    i += 1
  print(f'Глобальный минимум найден в точке x = {middle}; f(x) = {f(middle)}')

dihotomy(-2, 1)

from math import log

def iterations(a, b, epsilon=1e-3):
  sigma = epsilon / 4
  print('Кол-во операций: ', end='')
  print(
    log(
      (b - a - 2 * sigma) / (epsilon - 2 * sigma)
    ) / log(2)
  )

iterations(-2, 1)

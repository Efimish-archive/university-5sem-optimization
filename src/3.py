def f(x):
  return (2 * x * (2 * x + 3)) / (x**2 + 4 * x + 5)

# Метод поразрядного поиска
def bitwise(a, b, epsilon=1e-3):
  h = (b - a) / 4
  x0 = a
  steps = 0
  while True:
    fx0 = f(x0)
    x1 = x0 + h
    fx1 = f(x1)
    steps += 1
    if not (a <= x1 <= b):
      if abs(h) <= epsilon:
        print(f"За {steps} операций мы нашли f({x0})={fx0}")
        break
      else:
        h = -h/4
        if x1 <= a:
          x0 = a
        else:
          x0 = b
        continue

    if fx0 > fx1:
      x0 = x1
    else:
      if abs(h) <= epsilon:
        print(f"За {steps} операций мы нашли f({x0})={fx0}")
        break
      else:
        x0 = x1
        h = -h/4

bitwise(-2, 1)

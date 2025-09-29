def f(x):
  return (2 * x * (2 * x + 3)) / (x**2 + 4 * x + 5)

def bitwise(a, b, epsilon=1e-3):
  h = (b - a) / 4
  x = a
  while abs(h) > epsilon:
    x2 = x + h
    if f(x) < f(x2):
      h = -(h / 4)
    x = x2
  return x

print(bitwise(-2, 1))

# from math import exp

# def f(x):
#   return exp(-2*x) + (x**2)/2

# # Метод секущих
# def secant(a, b, epsilon=1e-3):
#   pass

# secant(0, 2)


# from sympy import symbols,Derivative
# import sympy
# from math import exp

# def f_div(value):
#     x= symbols('x')
#     expr = sympy.exp(x) + (1/(x+2))
#     expr=sympy.diff(expr)
#     expr=expr.subs(x,value).evalf()
#     return expr

# def f(x):
#     expr = exp(x)+(1/(x+2))
#     return expr
# def hordfunc(a,b,sigm=0.0001):
#     #1
#     k=0
#     ak=a
#     bk=b
#     #2
#     while True:
#         xk1=ak-(bk-ak)*f_div(ak)/(f_div(bk)-f_div(ak))
#         fxk1=f_div(xk1)
#         print(f"{k} |f(Xk+1): {f(xk1)} | f(Xk+1)':{fxk1} | Xk+1:{xk1}")
#         #3
#         if abs(fxk1)<=sigm:
#             return fxk1
#         #4
#         else:
#             if fxk1>0:
#                 ak1=ak
#                 bk1=xk1
#             else:
#                 ak1=xk1
#                 bk1=bk
#             k+=1
#             ak=ak1
#             bk=bk1
# hordfunc(-1,1)

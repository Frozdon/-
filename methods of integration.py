import math
import matplotlib.pyplot as plt
import numpy as np
def func(x,a):
    return (a*x - math.cos(x)/math.sin(x))
def derfunc(x,a):
    return(a+1/((math.sin(x))**2))
#метод ньютона
def res(a):
    x=0.1
    while abs(func(x,a))>0.0000001:
        x=x-func(x,a)/derfunc(x,a)
    return(x)
#зададим начальные значения точек
n=200
#формула трапеций
def integrate_trap(a1,a2):
    Integral=0
    h=(abs(a1-a2))/n
    for i in range(n-1):
        Integral= Integral + h*(res(a1+i*h)+res(a1+(i+1)*h))/2
    return Integral
#формула средних
def integrate_middle(a1,a2):
    Integral=0
    h=(abs(a1-a2))/n
    for i in range(n-1):
        Integral= Integral + (h)*res(a1 + 0.5*(h*i + h*(i+1)))
    return Integral
#формула Симспона и Боде
def integrate_simpson(a1,a2):
  Integral=0
  h=(abs(a1-a2))/n
  for i in range(n):
    b=a1+(i+1)*h
    a=a1+i*h
    Integral = Integral + ((b-a)/6)*(res(a) + 4*res((a+b)/2)+res(b))
  return(Integral)
x1=0
x2=2
print(integrate_trap(x1,x2))
print(integrate_middle(x1,x2))
print(integrate_simpson(x1,x2))
#make data
h=(abs(x1-x2))/n
masx=[]
mastrap=[]
masmiddle=[]
massimpson=[]
for i in range(n):
    masx.append(x1+i*h)
    mastrap.append(integrate_trap(x1,x1+i*h))
    masmiddle.append(integrate_middle(x1,x1 + i*h))
    massimpson.append(integrate_simpson(x1,x1 + i*h))
plt.style.use('_mpl-gallery')
# plot
fig, ax = plt.subplots()

ax.plot(masx, mastrap, linewidth=2.0)

ax.set(xlim=(x1,x2), xticks=np.arange(x1, x2),
       ylim=(0, 2), yticks=np.arange(0, 2))
plt.show()
# plot
fig, ax = plt.subplots()

ax.plot(masx, masmiddle, linewidth=2.0)

ax.set(xlim=(x1,x2), xticks=np.arange(x1, x2),
       ylim=(0, 3), yticks=np.arange(0, 3))
plt.show()
# plot
fig, ax = plt.subplots()

ax.plot(masx, massimpson, linewidth=2.0)

ax.set(xlim=(x1,x2), xticks=np.arange(x1, x2),
       ylim=(0, 3), yticks=np.arange(0, 3))
plt.show()

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from random import uniform


# function that returns dz/dt
def model_m(z,t):
    x = z[0]
    y = z[1]
    z = z[2]
    dxdt = 35*(y-x)
    dydt = -7*x-x*z+28*y
    dzdt = x*y - 3*z
    dVdt = [dxdt,dydt,dzdt]
    return dVdt

def model_s(z,t,u):
    x = z[0]
    y = z[1]
    z = z[2]
    dxdt = 35*(y-x)
    dydt = -7*x-x*z+28*y+u
    dzdt = x*y - 3*z
    dVdt = [dxdt,dydt,dzdt]
    return dVdt

# initial condition
z0m = [ 7, 0.7, 10]
z0s = [ 3, 0.5, 1.0]

# number of time points
n = 500000

# time points
t = np.linspace(0,20,n)

# step input
u = np.zeros(n)

# store solution
xm = np.empty_like(t)
ym = np.empty_like(t)
zm = np.empty_like(t)

xs = np.empty_like(t)
ys = np.empty_like(t)
zs = np.empty_like(t)

# record initial conditions
xm[0] = z0m[0]
ym[0] = z0m[1]
zm[0] = z0m[2]

xs[0] = z0s[0]
ys[0] = z0s[1]
zs[0] = z0s[2]

# solve ODE
for i in range(1,n):
    # span for next time step
    tspan = [t[i-1],t[i]]
    # solve for next step
    Vm = odeint(model_m, z0m, tspan)
    # store solution for plotting
    xm[i] = Vm[1][0]
    ym[i] = Vm[1][1]
    zm[i] = Vm[1][2]
    # next initial condition
    z0m = Vm[1]

    u[i] = -2.5*(ys[i-1] - ym[i-1])

    Vs = odeint(model_s, z0s, tspan, args=(u[i],))
    # store solution for plotting
    xs[i] = Vs[1][0] 
    ys[i] = Vs[1][1] 
    zs[i] = Vs[1][2]
    # next initial condition
    z0s = Vs[1] 

input_system = np.zeros(n)

l = n//10

for i in range(l):
    input_system[int((i+0.5)*l):(i+1)*l] = 20

output_system = input_system + (xm - xs)
'''
plt.plot(t, xs, 'b', label = 'original')
plt.plot(t, xm, 'r', label = 'mensagem codificada')
plt.legend()
'''

plt.xlabel('Tempo (s)', fontsize=16 )
plt.ylabel('Mensagens',fontsize=16)
plt.title(r"Entrada/Saida", fontsize=20)

plt.plot(t, input_system, 'b', label = 'Original')
plt.plot(t, output_system, 'r', label = 'Saida')

plt.legend()

plt.show()

plt.xlabel('Tempo (s)', fontsize=16 )
plt.ylabel('Mensagens',fontsize=16)
plt.title(r"Entrada/Saida", fontsize=20)

plt.plot(t, input_system, 'b', label = 'original')
plt.plot(t, input_system+xm, 'r', label = 'mensagem codificada')
plt.legend()

plt.show()
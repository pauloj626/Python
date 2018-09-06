import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# function that returns dz/dt
def model(z,t,u):
    x = z[0]
    y = z[1]
    z = z[2]
    dxdt = 35*(y-x)
    dydt = -7*x-x*z+28*y
    dzdt = x*y - 3*z
    dVdt = [dxdt,dydt,dzdt]
    return dVdt

# initial condition
z0 = [7,0.7, 10]

# number of time points
n = 10000

# time points
t = np.linspace(0,20,n)

# step input
u = np.zeros(n)
# change to 2.0 at time = 5.0
u[51:] = 2.0

# store solution
x = np.empty_like(t)
y = np.empty_like(t)
z = np.empty_like(t)
# record initial conditions
x[0] = z0[0]
y[0] = z0[1]
z[0] = z0[2]

# solve ODE
for i in range(1,n):
    # span for next time step
    tspan = [t[i-1],t[i]]
    # solve for next step
    V = odeint(model,z0,tspan,args=(u[i],))
    # store solution for plotting
    x[i] = V[1][0]
    y[i] = V[1][1]
    z[i] = V[1][2]
    # next initial condition
    z0 = V[1] 

# plot results
fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot(x, y, z, label='parametric curve')
ax.legend()

plt.show()
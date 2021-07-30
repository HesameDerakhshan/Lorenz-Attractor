import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

rho = 28.0
sigma = 10.0
beta = 8.0 / 3.0




def model(state, t):
    x, y, z = state           # Unpack the state vector
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return dxdt, dydt, dzdt   # Derivatives

state0 = [1.0, 1.0, 1.0]      # Initial condition
time = np.arange(0.0, 30.0, 0.01)

states = odeint(model, state0, time)

plt.ion()
fig = plt.figure()
fig.canvas.set_window_title('Lorenz')
fig = plt.figure()
ax = fig.gca(projection="3d")
x = states[:, 0]
y = states[:, 1]
z = states[:, 2]
ax.plot(x, y, z)
ax.scatter(x[1], y[1], z[1], c="b", s=6)

lag =20
for i in range(len(x)):
    ax.scatter(x[i+lag], y[i+lag], z[i+lag], c="b", s=5)
    
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.pause(0.001)

plt.draw()
plt.show()
    

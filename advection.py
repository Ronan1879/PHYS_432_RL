"""
Advection equation
FTCS and Lax-Friedrich methods

@author: Ronan Legin
Feb. 28th 2020
"""

# Include necessary packages
import numpy as np
import matplotlib.pyplot as plt

# Evolve f with the ftcs method
def evolve_ftcs(f,u,dx,dt):
    # By only changing the values within domain and not on boundary
    # i.e not f[0] or f[-1], then I'm keeping the boundary fixed.
    f[1:-1] = f[1:-1] - u*dt/(2*dx)*(f[2:] - f[:-2])
    return f

# Evolve f with the Lax-Friedrich method
def evolve_lax(f,u,dx,dt):
    f[1:-1] = -u*dt/(2*dx)*(f[2:]-f[:-2]) + 1/2*(f[2:] + f[:-2])
    return f

# Initialize scalar quantities
npix = 1000
u = -0.1
dx = 1.0
dt = dx/(40.0*np.abs(u))
steps = 70000

# Code for plotting
plt.ion()
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.set_title("FTCS")
ax1.set_xlabel("x",fontsize=14)
ax1.set_ylabel("f(x)",fontsize=14)
ax2.set_title("LAX")
ax2.set_xlabel("x",fontsize=14)
fig.set_size_inches(6, 5)
fig.canvas.draw()

# Initialize our function f for both ftcs and Lax-Friedrich methods
x = np.arange(0,npix)*dx
f_ftcs = np.arange(0,npix)*dx
f_lax = np.arange(0,npix)*dx

p1, = ax1.plot(x,f_ftcs)
p2, = ax2.plot(x,f_lax)

for n in np.arange(0,steps):
    # First and only step is to evolve the function f using both methods
    f_ftcs = evolve_ftcs(f_ftcs,u,dx,dt)
    f_lax = evolve_lax(f_lax,u,dx,dt)

    if n%100 == 0:
        p1.set_ydata(f_ftcs)
        p2.set_ydata(f_lax)
        fig.canvas.draw()
        plt.pause(0.01)
"""
1-Dimensional Hydro solver

@author: Ronan Legin
Feb. 28th 2020
"""

# Include necessary packages
import numpy as np
import matplotlib.pyplot as plt

# Define our gaussian initial perturbation function
def gaussian(x,mean,std,f0):
    return np.exp(-((x-mean)/std)**2) + f0

# Evolve quantity f1 or f2 without added source
def evolve_f(f,J,alpha):
    f[1:npix-1] = f[1:npix-1] - alpha*(J[1:npix-1] - J[:npix-2])

# Apply reflective boundary on f1 or f2
def apply_bc(f,J,alpha):
    f[0] = f[0] - alpha*J[0]
    f[-1] = f[-1] + alpha*J[-1]

# Add source term to f2
def apply_source(f1,f2,alpha,cs):
    f2[1:npix-1] = f2[1:npix-1] - alpha*cs**2*(f1[2:] - f1[:npix-2])

# Get the J flux array for f1 or f2
def get_J(f,u,alpha):
    J = np.zeros(npix-1)
    ind = np.where(u > 0)[0]
    J[ind] = u[ind]*f[ind]
    ind = np.where(u < 0)[0]
    J[ind] = u[ind]*f[ind+1]

    return J

# Define our scalar quantities
npix = 5000
dx = 0.02
dt = 0.00001
alpha = dt/dx
cs = 343
steps = 120000

# Initialize arrays for our important quantities
f1 = np.zeros(npix)
f2 = np.zeros(npix)
u = np.zeros(npix-1)

# Create array containing position x
x = np.arange(npix)*dx

# Calculate mean, standard deviation and gaussian y axis offset
# The f0 offset is mainly introduced to avoid any divergence due to
# f2/f1 to find velocity u.
# The numerical value of these quantities is arbitrary
mean = np.mean(x)
std = x[-1]/20
f0 = 8

# Initiliaze f1 with gaussian and calculate f2
f1 = 0.1*gaussian(x,mean,std,f0)
f2[:-1] = f1[:-1]*u

# Code to create figure canvas
plt.ion()
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.set_title("F1 (Density)")
ax1.set_xlabel("x",fontsize=14)
ax1.set_ylabel("f1(x)",fontsize=14)
ax2.set_title("F2/F1 (Velocity)")
ax2.set_xlabel("x",fontsize=14)
fig.set_size_inches(6, 5)
fig.canvas.draw()

# Plot first f1 and velocity field (f2/f1) at initial time
p1, = ax1.plot(x,f1)
p2, = ax2.plot(x,f2/f1)

# Begin loop over all time steps
for n in np.arange(steps):
    # First, we compute the velocity by averaging between adjacent velocity cell grids
    u = (f2[0:npix-1]/f1[0:npix-1] + f2[1:npix]/f1[1:npix])/2

    # Second, we get our J flux arrays for f1 and f2
    J1= get_J(f1,u,alpha)
    J2= get_J(f2,u,alpha)

    # Third, we evolve f1 and f2 by one time step. This does not include source term.
    evolve_f(f1,J1,alpha)
    evolve_f(f2,J2,alpha)

    # Fourth, we apply our source term to f2
    apply_source(f1,f2,alpha,cs)

    # Finally, we apply our reflective boundary conditions to both f1 and f2
    apply_bc(f1,J1,alpha)
    apply_bc(f2,J2,alpha)

    # Update plot at every 100 time step 
    if n % 100 == 0:
        p1.set_ydata(f1)
        p2.set_ydata(f2/f1)
        # The y limit is in place to adapt plotting range
        ax2.set_ylim(-2*np.max(f2/f1),2*np.max(f2/f1))
        fig.canvas.draw()
        plt.pause(0.01)
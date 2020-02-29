# PHYS_432_RL
Contains assignement 4 for PHYS 432

Author : Ronan Legin

Python version : 3.x

Collaborators: Alex Khoury, Mathieu Bruneault

This github repository contains two python scripts : hydro.py and advection.py

## Files
advection.py : Contains code to run simulation of advection equation without diffusion. Running the script will show a simulation of advection with the plot being updated every 100 time steps in real time. To run, type in terminal "python advection.py"

hydro.py : Contains code to run the 1-Dimensional Hydro solver. Running the script will show a simulation of 1D Hydro using the donor cell advection scheme with the plot being updated in real time. To run, type in terminal "python hydro.py"

## Problem questions
# Advection :
We notice that the FTCS method is highly unstable while the Lax-Friedrich scheme remains stable for the whole duration of the simulation

# 1D Hydro :
Initially, our gaussian perturbation splits in the middle and both oppositely travelling waves reach boundary and get reflected back towards center. I notice that once they come back together, if the initial density amplitude was high enough, then once they merge together, a sharp jump in density happens in the center which represents a shock. When the amplitude of the initial density perturbation is much smaller, we would instead see more of a smooth increase in density when the two waves merge which would be similar looking to the initial gaussian perturbation. Now for the width of shock wave, I notice that this was dependent on the velocity. Higher velocity made the shock wave thinner while lower velocity made the shock upon collision wider.

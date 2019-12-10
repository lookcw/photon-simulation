import random
import numpy as np
import matplotlib.pyplot as plt
from Prt import Prt

def run_simulation(n_steps, mu):

    n_particles_initial = 50
    n_particles_new = 10
    lx = 10
    ly = 20

    particles = []
    for i in range(n_particles_initial):
        px_init = random.uniform(-1,1)
        particles.append(Prt(px_init,0,lx,ly))

    n_detected = 0

    for n in range(n_steps):

        for p in particles:
            p.update_pos(mu)

            if p.is_detected:
                n_detected += 1

        # remove dead particles
        particles = [p for p in particles if not p.is_dead]


        # add new particles at each time step
        for i in range(n_particles_new):
            px_init = random.uniform(-1,1)
            particles.append(Prt(px_init,0,lx,ly))

    return n_detected


n_steps = 100

# create different mu values
fs = 50 # sample rate 
f = 2 # the frequency of the signal

x = np.arange(fs) # the points on the x axis for plotting
# compute the value (amplitude) of the sin wave at the for each sample
amp = 3
mu_list = amp + amp*np.sin(2*np.pi*f * (x/fs))

result_detected = []

for mu in mu_list:
    n_detected = run_simulation(n_steps, mu)
    result_detected.append(n_detected)


# plot particles detected over different mu values
plt.plot(mu_list,result_detected)
plt.show()
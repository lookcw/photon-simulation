import random
import numpy as np
import matplotlib.pyplot as plt
from Prt import Prt

def run_simulation(n_steps, mu_list):

    n_particles_initial = 50
    n_particles_new = 10
    lx = 500
    ly = 100

    particles = []

    for i in range(n_particles_initial):
        px_init = random.uniform(-1,1)
        particles.append(Prt(px_init,0,lx,ly))

    n_detected_list = []
    avg_angle_list = []

    for n in range(n_steps):
        print(n)
        n_detected = 0
        angles = []

        for p in particles:
            p.update_pos(mu_list[n])
            p.update_dead()
            angles.append(p.angle)

            if p.is_detected:
                n_detected += 1

        # remove dead particles
        particles = [p for p in particles if not p.is_dead]

        # calculate average angle
        avg_angle = sum(angles) / len(angles) 
        avg_angle_list.append(avg_angle)

        # add new particles at each time step
        for i in range(n_particles_new):
            px_init = random.uniform(-1,1)
            particles.append(Prt(px_init,0,lx,ly))

        n_detected_list.append(n_detected)
    return n_detected_list, avg_angle_list


n_steps = 2000

# create different mu values
fs = 1000 # sample rate 
f = 1 # the frequency of the signal


x = np.arange(n_steps) # the points on the x axis for plotting
# compute the value (amplitude) of the sin wave at the for each sample
amp = 3
mu_list = amp + amp*np.sin(2*np.pi*f * (x/fs))


n_detected_list, avg_angle_list = run_simulation(n_steps, mu_list)

avg_n = 10

def moving_average(a, n=avg_n):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

n_detected_avg = moving_average(n_detected_list)

# plot mu values
plt.plot(x/fs,mu_list, label='Attenuation Coefficient (mu)')
# plt.show()

# plot particles detected over different mu values
#plt.plot(n_detected_list)
plt.plot(x[:-avg_n+1]/fs,n_detected_avg, label ='Number of Photons Detected (moving average)')
plt.xlabel('Simulation Time (seconds)')
plt.legend()
plt.show()

plt.plot(x/fs,avg_angle_list)
plt.xlabel('Simulation Time (seconds)')
plt.ylabel('Average Photon Velocity Angle (degrees)')
plt.show()
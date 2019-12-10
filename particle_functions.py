import numpy as np

def choose_new_angle(Vx,Vy,std):
	old_angle = np.arctan(Vy/Vx)
	old_angle = np.degrees(old_angle)

	mu = 0.0
	refraction = np.random.normal(loc=mu, scale=std, size=None)

	new_angle = old_angle + refraction
	new_angle = radians(new_angle)

	newVx = 1.0*np.cos(new_angle)
	newVy = 1.0*np.sin(new_angle)
	
	return (newVx,newVy)
import numpy as np

def choose_new_angle(Vx,Vy,std):
	old_angle = np.arctan(Vy/Vx) if Vx != 0 else np.pi/2
	old_angle = np.degrees(old_angle)

	mu = 0.0
	refraction = np.random.normal(loc=mu, scale=std, size=None)

	new_angle = old_angle + refraction
	new_angle = np.radians(new_angle)

	newVx = 1.0*np.cos(new_angle)
	newVy = 1.0*np.sin(new_angle)
	
	return (newVx,newVy)
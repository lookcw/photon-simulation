from particle_functions import choose_new_angle
from random import uniform
from math import exp

class Prt:

    def __init__(self,px,py,lx,ly):
        self.lx, self.ly = lx,ly
        self.px, self.py = px , py
        (self.vx,self.vy) = choose_new_angle(0,1,50)
        self.is_dead = False
        self.is_detected = False

    def update_dead(self):
        if self.py < 0:
            self.is_detected = True
            self.is_dead = True
        elif self.px > self.lx / 2 or self.px < -self.lx / 2 or self.py > self.ly :
            self.is_dead = True
    
    def _take_step(self):
        self.px += self.vx
        self.py += self.vy

    def update_pos(self, u):
        rand = uniform(0,1)
        death_thresh = exp(-u)
        if rand < death_thresh:
            self.is_dead = True
        else:
            angle_thresh = exp(-u/2)
            if rand < angle_thresh:
                (self.vx,self.vy) = choose_new_angle(50)
            self._take_step()
        
            
            


     

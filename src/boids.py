import random


class Boid():
    def __init__(self, id) -> None:
        self.id = id
        self.x = random.randint(0, 500)
        self.y = random.randint(0, 500)
        self.vx = random.randint(-10, 10)
        self.vy = random.randint(-10, 10)
    
    def get_x(self):
        return self.x
    
    def set_x(self, x):
        self.x = x
    
    def get_y(self):
        return self.y
    
    def set_y(self, y):
        self.y = y 
    
    def get_vx(self):
        return self.vx
    
    def set_vx(self, vx):
        self.vx = vx
    
    def get_vy(self):
        return self.vy
    
    def set_vy(self, vy):
        self.vy = vy
    
    def get_id(self):
        return self.id
    
    
    
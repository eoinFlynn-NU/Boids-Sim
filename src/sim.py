from boids import Boid




class Sim():
    def __init__(self, separation: int, alignment: int, cohesion: int) -> None:
        self.separation = separation
        self.alignment = alignment
        self.cohesion = cohesion
        self.boids = [Boid(i) for i in range(50)]
        self.protected_range = 10
        self.visible_range = 50
    
    
    
    def cohesion_boid(self, boid: Boid):
        xpos_avg = 0
        ypos_avg = 0
        neighboring_boids = 0
        for ob in self.boids:
            if ob.get_id() != boid.get_id():
                dx = boid.get_x() - ob.get_x()
                dy = boid.get_y() - ob.get_y()
                if dx**2 + dy**2 < self.visible_range**2:
                    xpos_avg += ob.get_x()
                    ypos_avg += ob.get_y()
                    neighboring_boids += 1
        xpos_avg /= neighboring_boids
        ypos_avg /= neighboring_boids
        boid.set_vx(xpos_avg-boid.get_x())*self.cohesion
        boid.set_vy(ypos_avg-boid.get_y())*self.cohesion


    def align_boid(self, boid:Boid):
        xvel_avg = 0
        yvel_avg = 0
        neighboring_boids = 0
        for ob in self.boids:
            if ob.get_id() != boid.get_id():
                dx = boid.get_x() - ob.get_x()
                dy = boid.get_y() - ob.get_y()
                if dx**2 + dy**2 < self.visible_range**2 and dx**2 + dy**2 > self.protected_range:
                    xvel_avg += ob.get_vx()
                    yvel_avg += ob.get_vy()
                    neighboring_boids += 1
        xvel_avg /= neighboring_boids
        yvel_avg /= neighboring_boids
        boid.set_vx(xvel_avg-boid.get_vx())*self.alignment
        boid.set_vy(yvel_avg-boid.get_vy())*self.alignment



    def separate_boid(self, boid: Boid):
        close_dx = 0
        close_dy = 0
        for ob in self.boids:
            if ob.get_id() != boid.get_id():
                dx = boid.get_x() - ob.get_x()
                dy = boid.get_y - ob.get_y()
                if dx**2 + dy**2 < self.protected_range**2:
                    close_dx += dx
                    close_dy += dy
        
        boid.set_vx(boid.get_vx() + close_dx*self.separation)
        boid.set_vy(boid.get_vy() + close_dy*self.separation)
    
    
    

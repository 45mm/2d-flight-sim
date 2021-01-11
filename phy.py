import math

def PlanePhy(self, liftc, dragc):
  wingarea=(self.rect.w)*(math.cos(self.angle))+(self.rect.h)*(math.sin(self.angle))
  dragarea=(self.rect.h)*(math.cos(self.angle))+(self.rect.w)*(math.sin(self.angle))
  drag = (dragc*(self.vel.x**2)*dragarea)/2
  lift =  (liftc*(self.vel.y**2)*wingarea)/2
  self.vel.x=(self.vel.x)-drag
  self.vel.y=(self.vel.y)+lift
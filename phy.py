import math

def PlanePhy(self, liftc, dragc, gravity, HEIGHT):
  
  if self.rect.y < HEIGHT-self.rect.height:
      self.vel.y+=gravity

  wingarea=abs(math.cos(self.angle))
  dragarea=abs(math.sin(self.angle))
  drag = dragc*(self.vel.x**2)*dragarea
  lift =  liftc*(self.vel.y**2)*wingarea
  self.vel.x=(self.vel.x)-drag
  if self.rect.y>self.rect.height:
    self.vel.y=(self.vel.y)-lift
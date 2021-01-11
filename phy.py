import math

def PlanePhy(self, liftc, dragc, gravity, SCREEN_HEIGHT):
  
  if self.rect.y < SCREEN_HEIGHT-self.rect.height:
      self.vel.y+=gravity

  wingarea=math.abs(math.cos(self.angle))
  dragarea=math.abs(math.sin(self.angle))
  drag = dragc*(self.vel.x**2)*dragarea
  lift =  liftc*(self.vel.y**2)*wingarea
  self.vel.x=(self.vel.x)-drag
  if self.rect.y>self.rect.height:
    self.vel.y=(self.vel.y)-lift
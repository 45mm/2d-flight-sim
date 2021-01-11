import math

def PlanePhy(self, liftc, dragc, gravity, HEIGHT):
  
  if self.rect.y < HEIGHT-self.rect.height:
      self.vel.y+=gravity

  wingarea=(math.cos(self.angle))
  dragarea=(math.sin(self.angle))

  drag = pygame.Vector2(x,y)

  lift = liftc*(self.vel.y**2)*wingarea
  d=dragc*(self.vel.magnitude_squared())
  drag = pygame.math.Vector2(d*self.vel.x,d*self.vel.y)
  # drag = self.vel.normalize()*self.vel.magnitude_squared()*dragc
  if self.vel.magnitude()>0:
    self.vel = self.vel-drag
  if self.rect.y>self.rect.height:
    self.vel.y=(self.vel.y)-lift
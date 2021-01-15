import math
import pygame

def PlanePhy(self, liftc, dragc, gravity, HEIGHT, toRun):
  
  # if self.vel.x>5:
  #   self.vel.x = 5
  # elif self.vel.x <= -5:
  #   self.vel.x = -5
  # if self.vel.y > 5:
  #   self.vel.y = 5
  # elif self.vel.y < -5:
  #   self.vel.y = -5

  angle = math.radians(self.angle)-math.pi
    
  if self.rect.y < HEIGHT-self.rect.height:
    self.vel += pygame.math.Vector2(0, gravity)
      
  # wingarea = 0.1 + abs(math.cos(self.angle))
  # dragarea = 0.1 + abs(math.sin(self.angle))
  wingarea = 0.1 + abs(math.cos(angle))
  # dragarea = 1.1
  p = math.atan2(-self.vel.y,self.vel.x)
  dragarea=0.1+abs(math.sin(p-angle))
  print('Angles: ', p, '-', angle)
  print("sine: ", math.sin(p-angle))

  lift = liftc*(abs(self.vel.x**2))*wingarea
  if lift > gravity:
    lift = gravity
    
  # lift = (self.vel.normalize().rotate(90)) *self.vel.magnitude_squared()*liftc*wingarea

  # lift = (self.vel.normalize().rotate(90)) *self.vel.magnitude()*liftc*wingarea

  # lift = pygame.Vector2(0,0) #only for testing. I am definitely not just giving up.

  # d=dragc*(self.vel.magnitude_squared())*dragarea
  # drag = pygame.math.Vector2(d*self.vel.x,d*self.vel.y)

  drag = self.vel.normalize()*self.vel.magnitude_squared()*dragc*dragarea


  # def new_normalize(vec):

  #   if vec.magnitude()==0:
  #     return pygame.Vector2(0,0)
  #   else:
  #     return vec.normalize()
  
  # if drag[1] > 1.0 :
  #   drag[1] = 1.0
  # elif drag[0] < -1.0:
  #   drag[0] = -1.0
  # elif drag[1] < -1.0:
  #   drag[1] = -1.0
  # elif drag[0] > 1.0:
  #   ag[0] = 1.0

  # print('Dragarea:', dragarea, 'Drag:',new_normalize(drag), 'Vel:',new_normalize(self.vel), end = ' ')
  print('Wingarea:', wingarea, 'Lift:',lift, 'Vel_mag:',self.vel.magnitude(), "angle:", self.angle)
  print('Dragarea:', dragarea, 'Drag:',drag, 'Vel:',self.vel, "angle:", self.angle, end = ' ')
  
  # if (self.vel.magnitude()-drag.magnitude()) > 0:
  if abs(self.vel.y) - abs(drag.y)>0 and abs(self.vel.x) - abs(drag.x) >0:
    self.vel = self.vel - drag
    print('Done')
  else:
    print()
    
# if self.rect.y>self.rect.height:
  self.vel.y=(self.vel.y)-lift
    # self.vel = self.vel - lift
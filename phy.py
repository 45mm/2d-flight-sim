import math
import pygame
from constants import SCREEN_HEIGHT, LIFTC, DRAGC, GRAVITY

def PlanePhy(self, toRun=True):
  
  # if self.vel.x>5:
  #   self.vel.x = 5
  # elif self.vel.x <= -5:
  #   self.vel.x = -5
  # if self.vel.y > 5:
  #   self.vel.y = 5
  # elif self.vel.y < -5:
  #   self.vel.y = -5

  angle = math.radians(self.angle)
    
  if self.rect.y < SCREEN_HEIGHT-self.rect.height:
    self.vel += pygame.math.Vector2(0, GRAVITY)
      
  # wingarea = 0.1 + abs(math.cos(self.angle))
  # dragarea = 0.1 + abs(math.sin(self.angle))
  wingarea = 0.1 + abs(math.cos(angle))
  # dragarea = 1.1
  vel_angle = math.atan2(-self.vel.y,self.vel.x) #Angle of velocity
                                                              #vector
  
  p = vel_angle if vel_angle >= 0 else vel_angle + math.pi*2

  dragarea=0.1+abs(math.sin(p-angle))
  '''print('Angles: ', p, '-', angle)
  print("sine: ", math.sin(p-angle))
  print('Diff: ', p-angle)'''

  lift = LIFTC*(abs(self.vel.x**2))*wingarea
  if lift > GRAVITY:
    lift = GRAVITY
    
  # lift = (self.vel.normalize().rotate(90)) *self.vel.magnitude_squared()*LIFTC*wingarea

  # lift = (self.vel.normalize().rotate(90)) *self.vel.magnitude()*LIFTC*wingarea

  # lift = pygame.Vector2(0,0) #only for testing. I am definitely not just giving up.

  # d=DRAGC*(self.vel.magnitude_squared())*dragarea
  # drag = pygame.math.Vector2(d*self.vel.x,d*self.vel.y)

  drag = self.vel.normalize()*self.vel.magnitude_squared()*DRAGC*dragarea

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
  '''print('Wingarea:', wingarea, 'Lift:',lift, 'Vel_mag:',self.vel.magnitude(),"VEL", self.vel, "angle:", self.angle)'''
  #print('Dragarea:', dragarea, 'Drag:',drag, 'Vel:',self.vel, "angle:", self.angle, end = ' ')
  
  # if (self.vel.magnitude()-drag.magnitude()) > 0:
  if abs(self.vel.y) - abs(drag.y)>0 and abs(self.vel.x) - abs(drag.x) >0:
    self.vel = self.vel - drag
    '''print('Done')'''
  else:
    print()
    
# if self.rect.y>self.rect.height:
  self.vel.y=(self.vel.y)-lift
    # self.vel = self.vel - lift

#if self.y < 70:
    #lift = 0
    #self.vel.y += 1
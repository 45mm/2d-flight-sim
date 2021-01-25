import pygame , random
from constants import *

CollisionObjects = pygame.sprite.Group()

class Cloud(pygame.sprite.Sprite):
    
  def __init__(self,cloudSprite, x, y, w, h,cloudvelc):
    super().__init__()
    self.image = pygame.transform.scale(cloudSprite, (w, h))
    #self.rect = pygame.Rect(0, 0, w, h)
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.mask = pygame.mask.from_surface(self.image)    
    self.vel = pygame.math.Vector2(0,0)
    self.vel.x=(random.random())*cloudvelc
  def render(self, surface):
    surface.blit(self.image, (self.rect.x, self.rect.y))
  def update(self, screen, playerclass):
    playervelx = playerclass.vel.x
    
    self.rect.x += self.vel.x
    self.rect.y += self.vel.y
    CollisionObjects.add(self)    
    
class Birds(pygame.sprite.Sprite):
    
  def __init__(self, birdSprite, x, y, w, h, birdvelx, birdvely):
    super().__init__()
    self.image = pygame.transform.scale(birdSprite, (w, h))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.mask = pygame.mask.from_surface(self.image)    
    self.vel = pygame.math.Vector2(2,2)

  def update(self, screen):
    birdvelx = 4
    birdvely = 2
    self.rect.x += self.vel.x
    self.rect.y += self.vel.y
    
    if self.rect.y < 50:
      self.vel = pygame.math.Vector2(birdvelx, birdvely)

    if self.rect.y == 100 and self.vel.y<0:
      self.vel = pygame.math.Vector2(birdvelx, -birdvely)

    if self.rect.y == 100 and self.vel.y>0:
      self.vel = pygame.math.Vector2(birdvelx, birdvely)
  
    if self.rect.y > 300:
      self.vel = pygame.math.Vector2(birdvelx, -birdvely)

    if self.rect.x >= (SCREEN_WIDTH - self.rect.w) or self.rect.x <= 0:
      self.rect.x = 100
      self.rect.y = 100
      
    CollisionObjects.add(self)
    
  def render(self, surface):
    surface.blit(self.image, (self.rect.x, self.rect.y))
    
    
class Terrain(pygame.sprite.Sprite):
  #IMP: NEEDS REAL SCREEN ATTRIBUTES
  def __init__(self, ground, surface):
    super().__init__()
    self.image = pygame.transform.scale (ground, (surface.get_width(), surface.get_height()))
    self.rect = self.image.get_rect()
    self.mask = pygame.mask.from_surface(self.image)
    CollisionObjects.add(self)

class Thrust():

  def __init__(self, angle, magnitude):
    self.dir = pygame.math.Vector2(1,0).rotate(angle)
    self.magnitude = magnitude

  def get_vec(self):
    return self.dir*self.magnitude
    

class Sprite(pygame.sprite.Sprite):

  def __init__(self,imageSprite, x, y, w, h, rot_angle, vel):
    super().__init__()
    self.x = x
    self.y = y
    self.image = pygame.transform.scale(imageSprite, (w,h))
    self.mask = pygame.mask.from_surface(self.image) # used if rough detection passes
    self.rect = pygame.Rect(0,0,w,h) #for rough collision detection
    self.rect.center = (self.x,self.y)
    # self.hitbox = self.mask.get_rect()
    self.origin = (self.rect.x, self.rect.y) #point at which to draw the image
    self.vel = vel
    self.thrust = Thrust(0, 0)
    
    self.thrustc = 0.01

    self.rot_angle = rot_angle # angle by which to rotate per frame
    self.angle = 0 # angle wrt x axis, counterclockwise
    self.RESTART_NEEDED = False
    self.MASK_NEEDED = False
    # Permanent copies of initial properties; do not modify

    self.IMAGE = self.image
    self.RECT = self.rect
    self.ANGLE = self.angle

  def rot_center(self, n): #n is either 1 or -1; for direction of rotation

    rot = n*self.rot_angle
    self.angle = (self.angle + rot) % 360

    rot_image = pygame.transform.rotate(self.IMAGE, self.angle)
    self.mask = pygame.mask.from_surface(rot_image, 0)
    rot_rect = rot_image.get_rect()

    # self.hitbox = self.mask.get_rect()
    # self.hitbox.center = self.rect.center

    rot_rect.center = self.rect.center

    self.rect = rot_rect
    self.image = rot_image
    
  def collisionMask (self, screen):
    
    collided = pygame.sprite.spritecollide(self, CollisionObjects, False, pygame.sprite.collide_mask)
    print(collided)
    #collidedmask = pygame.sprite.collide_mask(self, Cloud)
    #print(collidedmask)
    if collided != []:
      self.RESTART_NEEDED = True#(self.player, otherobjects, False)
      
  def collisionWindow(self, screen):
    
    if self.rect.x >= (SCREEN_WIDTH - self.rect.w) or self.rect.x <= 0:#self.rect.w:
      self.rect.x = SCREEN_WIDTH - self.rect.w
      self.RESTART_NEEDED = True
      print('sxm cvgbjhfenwdcihr')
      
    elif self.rect.y >= (SCREEN_HEIGHT - self.rect.h) or self.rect.y <= 0:#self.rect.h:
      self.rect.y = SCREEN_HEIGHT - self.rect.h
      self.RESTART_NEEDED = True
    
    elif self.rect.x <= 0:
      self.rect.x = 0
      
    elif self.rect.y <= 0:
      self.rect.y = 0
      
    

  def update(self, keys, KEYMAP, screen, toRun):
    
    if toRun:
      self.vel += self.thrust.get_vec()

      self.x += self.vel.x
      self.y += self.vel.y

      self.rect.center = (self.x, self.y)
      # self.hitbox.center = self.rect.center

      if keys[KEYMAP['tiltup']]:
        # self.vel = self.vel.rotate(-self.rot_angle)
        self.thrust.dir = self.thrust.dir.rotate(-self.rot_angle)
        self.rot_center(1)

      if keys[KEYMAP['tiltdown']]:
        # self.vel = self.vel.rotate(self.rot_angle)
        self.thrust.dir = self.thrust.dir.rotate(self.rot_angle)
        self.rot_center(-1)

      if keys[KEYMAP['accel']]:
        self.thrust.magnitude += self.thrustc
      if keys[KEYMAP['decel']]:
        if self.thrust.magnitude >= 0:
          self.thrust.magnitude -= self.thrustc

      self.collisionWindow(screen)
      #self.rect.clamp_ip(surface.get_rect())
      self.collisionMask(screen)

  def render(self, surface):

    #pygame.draw.rect(surface, (100,100,100), self.rect) #draw bounding rect for debugging
    # pygame.draw.rect(surface, (0,255,255), self.hitbox)
    pygame.draw.circle(surface, (255,255,0),(self.x, self.y), 5)
    pygame.draw.circle(surface, (255,0,0),(self.rect.center), 5)

    surface.blit(self.image, (self.rect.x, self.rect.y))

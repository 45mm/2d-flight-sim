import pygame , random
from constants import *

pygame.init()

cloudSprite = pygame.image.load("images/clouds_trans.png").convert_alpha()
birdSprite = pygame.image.load("images/bird.png").convert_alpha()

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

  def cloudspawn(camera, cameradist, Terrainclass):# ,safedist):
    safespawn = True
    x=random.random()*SCREEN_WIDTH#-((screen.get_width()/4)*random.random())
    # y=player.y+((random.random()-0.5)*VIEW_HEIGHT)
    y=SCREEN_HEIGHT/2 * random.random()
    # if <=0 or abs(player.y-y)<safedist:
    if camera.rect.left-cameradist<=x<=camera.rect.right+cameradist or camera.rect.top-cameradist<=y<=camera.rect.bottom+cameradist:
      safespawn=False
    # else:
    #   for cloud in cloudlist:
    #     if abs(cloud.rect.x-x)<=safedist  or abs(cloud.rect.y-y)<=safedist :
    #       safespawn=False
    #       break
    if safespawn==True:
      #print("spawn allowed")
      #cloud_args = {'cloudSprite':cloudSprite, 'x':SCREEN_WIDTH-((SCREEN_WIDTH/4)*random.random()), 'y':SCREEN_HEIGHT*random.random(), 'w':80, 'h':40, 'cloudvelc':5}
      cloudvar=Cloud(cloudSprite=cloudSprite, x=x, y=y, **CLOUD_ARGS)
      collidedmask = pygame.sprite.collide_mask(cloudvar, Terrainclass)
      #print(collidedmask)
      if collidedmask == None:
        cloudlist.append(cloudvar)
      
  def cloudupdate(surf, player):
    for cloudvar in cloudlist:
      cloudvar.update(surf,player)
      cloudvar.render(surf) 

class Bird(pygame.sprite.Sprite):
    
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

    if 0<=self.rect.y <= SCREEN_HEIGHT/2 and self.vel.y<0:
      self.vel = pygame.math.Vector2(birdvelx, -birdvely)

    if 0<=self.rect.y <= SCREEN_HEIGHT/2 and self.vel.y>0:
      self.vel = pygame.math.Vector2(birdvelx, birdvely)
  
    if self.rect.y >= SCREEN_HEIGHT/2:
      self.vel = pygame.math.Vector2(birdvelx, -birdvely)

    #if self.rect.x >= (SCREEN_WIDTH - self.rect.w) or self.rect.x <= 0:
     # self.rect.x = 100
      #self.rect.y = 100
      
    CollisionObjects.add(self)
    
  def render(self, surface):
    surface.blit(self.image, (self.rect.x, self.rect.y))

  def birdspawn(camera, cameradist, Terrainclass):
    safespawn = True
    x=random.random()*SCREEN_WIDTH
    y=SCREEN_HEIGHT/2 * random.random()
    if camera.rect.left-cameradist<=x<=camera.rect.right+cameradist or camera.rect.top-cameradist<=y<=camera.rect.bottom+cameradist:
      safespawn=False
      
    if safespawn==True:
      #print("spawn allowed")
      birdvar=Bird(birdSprite=birdSprite, x=x, y=y, **BIRD_ARGS)
      collidedmask = pygame.sprite.collide_mask(birdvar, Terrainclass)
      if collidedmask == None:
        birdlist.append(birdvar)
        
  def birdupdate(surf):
    for birdvar in birdlist:
      birdvar.update(surf)
      birdvar.render(surf)
    
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

  def __init__(self,imageSprite, x, y, w, h, rot_angle ):
    super().__init__()
    self.x = x
    self.y = y
    self.image = pygame.transform.scale(imageSprite, (w,h))
    self.mask = pygame.mask.from_surface(self.image) # used if rough detection passes
    self.rect = pygame.Rect(0,0,w,h) #for rough collision detection
    self.rect.center = (self.x,self.y)
    # self.hitbox = self.mask.get_rect()
    self.origin = (self.rect.x, self.rect.y) #point at which to draw the image
    self.vel = pygame.math.Vector2(0,0)
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
    
    plane_collided = pygame.sprite.spritecollide(self, CollisionObjects, False, pygame.sprite.collide_mask)
    #print(collided)
    #collidedmask = pygame.sprite.collide_mask(self, Cloud)
    if plane_collided != []:
      self.RESTART_NEEDED = True#(self.player, otherobjects, False)
      
  def collisionWindow(self, screen):
    
    if self.rect.x >= (SCREEN_WIDTH - self.rect.w) or self.rect.x <= 0:#self.rect.w:
      self.rect.x = SCREEN_WIDTH - self.rect.w
      self.RESTART_NEEDED = True
      
    elif self.rect.y >= (SCREEN_HEIGHT - self.rect.h) or self.rect.y <= 0:#self.rect.h:
      self.rect.y = SCREEN_HEIGHT - self.rect.h
      self.RESTART_NEEDED = True
    
    elif self.rect.x <= 0:
      self.rect.x = 0
      
    elif self.rect.y <= 0:
      self.rect.y = 0
      
    

  def update(self, keys, KEYMAP, screen, toRun,maxvel):
    
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
      #else:
      #  self.thrust.magnitude=0
      if keys[KEYMAP['decel']]:
        if self.thrust.magnitude >= 0:
          self.thrust.magnitude -= self.thrustc
      #else:
      #  self.thrust.magnitude=0
      #print(self.vel.magnitude)
      # if self.vel.magnitude>float(maxvel):
      #   self.vel.magnitude=maxvel
      # self.collisionWindow(screen)
      # #self.rect.clamp_ip(surface.get_rect())
      self.collisionMask(screen)

  def render(self, surface):

    #pygame.draw.rect(surface, (100,100,100), self.rect) #draw bounding rect for debugging
    # pygame.draw.rect(surface, (0,255,255), self.hitbox)
    pygame.draw.circle(surface, (255,255,0),(self.x, self.y), 5)
    pygame.draw.circle(surface, (255,0,0),(self.rect.center), 5)

    surface.blit(self.image, (self.rect.x, self.rect.y))

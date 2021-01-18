import pygame

CollisionObjects = pygame.sprite.Group() #LINE ADDED BY YASH
#CollisionObjects.add(self)    #LINE ADDED BY YASH
#self.mask = pygame.mask.from_surface(self.image)    #LINE ADDED BY YASH

class Cloud(pygame.sprite.Sprite):
    
  def __init__(self,imageSprite, x, y, w, h, vel):
    super().__init__()
    self.x = x
    self.y = y
    self.image = pygame.transform.scale(cloudSprite, (w, h))
    self.rect = pygame.Rect(0, 0, w, h)
    

  

  def render(self, surface):
    surface.blit(self.image, (self.rect.x, self.rect.y))
    pygame.display.flip()

  def update(self, keys, keymap, SCREEN_WIDTH, SCREEN_HEIGHT, toRun):
    vel = pygame.math.Vector2(-(get_(player.vel.x)), 0)
    
    #if

  #def 
'''    
class Birds(pygame.sprite.Sprite):
    
  def __init__(self, birdSprite, x, y, w, h, vel):
    super().__init__()
    self.x = x
    self.y = y
    self.image = pygame.transform.scale(x, y, w, h, vel)
    self.rect = pygame.Rect(0, 0, w, h)


  #def update(self):

  def render(self, surface):
    surface.blit(self.image, (self.rect.x, self.rect.y))
    pygame.display.flip()
'''   
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
    
    #collided = pygame.sprite.spritecollide(self, CollisionObjects, False, pygame.sprite.collide_mask)
    collidedmask = pygame.sprite.collide_mask(self, Cloud)
    if collidedmask != None:
      self.RESTART_NEEDED#(self.player, otherobjects, False)
      
  def collisionWindow(self, screen):
    
    if self.rect.x >= (screen.get_width() - self.rect.w) or self.rect.x <= 0:#self.rect.w:
      self.MASK_NEEDED = True
      
    elif self.rect.y >= (screen.get_height() - self.rect.h) or self.rect.y <= 0:#self.rect.h:
      self.MASK_NEEDED = True
    
    if self.rect.x >= screen.get_width()-self.rect.w:
      self.rect.x = screen.get_width() - self.rect.w
    
    elif self.rect.y >= screen.get_height() - self.rect.h:
      self.rect.y = screen.get_height() - self.rect.h
    
    elif self.rect.x <= 0:
      self.rect.x = 0
      
    elif self.rect.y <= 0:
      self.rect.y = 0
      
    

  def update(self, keys, keymap, screen, toRun):
    
    if toRun:
      self.vel += self.thrust.get_vec()

      self.x += self.vel.x
      self.y += self.vel.y

      self.rect.center = (self.x, self.y)
      # self.hitbox.center = self.rect.center

      if keys[keymap['tiltup']]:
        # self.vel = self.vel.rotate(-self.rot_angle)
        self.thrust.dir = self.thrust.dir.rotate(-self.rot_angle)
        self.rot_center(1)

      if keys[keymap['tiltdown']]:
        # self.vel = self.vel.rotate(self.rot_angle)
        self.thrust.dir = self.thrust.dir.rotate(self.rot_angle)
        self.rot_center(-1)

      if keys[keymap['accel']]:
        self.thrust.magnitude += self.thrustc
      if keys[keymap['decel']]:
        if self.vel.x >= 0:
          self.thrust.magnitude -= self.thrustc

      self.collisionWindow(screen)
      #self.rect.clamp_ip(surface.get_rect())
      self.collisionMask(screen)

  def render(self, surface):

    pygame.draw.rect(surface, (100,100,100), self.rect) #draw bounding rect for debugging
    # pygame.draw.rect(surface, (0,255,255), self.hitbox)
    pygame.draw.circle(surface, (255,255,0),(self.x, self.y), 5)
    pygame.draw.circle(surface, (255,0,0),(self.rect.center), 5)

    surface.blit(self.image, (self.rect.x, self.rect.y))
    pygame.display.flip()

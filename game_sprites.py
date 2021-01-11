import pygame

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
    self.rot_angle = rot_angle # angle by which to rotate per frame
    self.angle = 0 # angle wrt x axis, counterclockwise
    self.RESTART_NEEDED = False

    # Permanent copies of initial properties; do not modify

    self.IMAGE = self.image
    self.RECT = self.rect
    self.ANGLE = self.angle

  def rot_center(self, n): #n is either 1 or -1; for direction of rotation

    rot = n*self.rot_angle
    self.angle = (self.angle + rot) % 360

    rot_image = pygame.transform.rotate(self.IMAGE, self.angle)
    self.mask = pygame.mask.from_surface(rot_image)
    rot_rect = rot_image.get_rect()
    # self.hitbox = self.mask.get_rect()
    # self.hitbox.center = self.rect.center

    rot_rect.center = self.rect.center

    self.rect = rot_rect
    self.image = rot_image


  def handle_terrain_collision(self, SCREEN_WIDTH, SCREEN_HEIGHT):

    
    if self.rect.left < 0 and self.vel.x < 0:
      self.RESTART_NEEDED = True
      
    if self.rect.right > SCREEN_HEIGHT and self.vel.x > 0:
      self.RESTART_NEEDED = True
      
    if self.rect.top <= 0 and self.vel.y < 0:
      self.RESTART_NEEDED = True
      
    if self.rect.bottom >= SCREEN_WIDTH and self.vel.y > 0:
      self.RESTART_NEEDED = True
  

  def update(self, keys, keymap, SCREEN_WIDTH, SCREEN_HEIGHT):

    self.x += self.vel.x
    self.y += self.vel.y

    self.rect.center = (self.x, self.y)

    if keys[keymap['tiltup']]:
      self.vel = self.vel.rotate(-self.rot_angle)
      self.rot_center(1)

    if keys[keymap['tiltdown']]:
      self.vel = self.vel.rotate(self.rot_angle)
      self.rot_center(-1)

    self.handle_terrain_collision(SCREEN_WIDTH, SCREEN_HEIGHT)


  def render(self, surface):

    pygame.draw.rect(surface, (100,100,100), self.rect) #draw bounding rect for debugging
    # pygame.draw.rect(surface, (0,255,255), self.hitbox)
    pygame.draw.circle(surface, (255,255,0),(self.x, self.y), 5)
    pygame.draw.circle(surface, (255,0,0),(self.rect.center), 5)

    surface.blit(self.image, (self.rect.x, self.rect.y))
    pygame.display.flip()

    
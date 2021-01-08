def mainloop(): 
  keys = pygame.key.get_pressed()
  player.update(keys)
  player.render()

  # print(player.vel.magnitude())

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()

  pygame.display.update()
  screen.fill((0,0,0))
  clock.tick(60)
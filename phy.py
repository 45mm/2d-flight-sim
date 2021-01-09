def PlanePhy(liftc, dragc, fluidDensity):
  fluidDensity = 1.225 #si units
  wingarea=(player.w)*(math.cos(player.angle)))+(player.h)*(math.sin(player.angle)))
  dragarea=
  drag = (fluidDensity*dragc*(player.vel.x**2)*dragarea)/2
  lift =  (liftc*fluidDensity*(player.vel.y**2)*wingarea)/2
  player.vel.x=(player.vel.x)-drag
  player.vel.y=(player.vel.y)+lift
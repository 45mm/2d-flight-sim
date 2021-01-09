def PlanePhy(liftc, dragc):
  wingarea=(player.w)*(math.cos(player.angle)))+(player.h)*(math.sin(player.angle)))
  dragarea=(player.h)*(math.cos(player.angle)))+(player.w)*(math.sin(player.angle)))
  drag = (dragc*(player.vel.x**2)*dragarea)/2
  lift =  (liftc*(player.vel.y**2)*wingarea)/2
  player.vel.x=(player.vel.x)-drag
  player.vel.y=(player.vel.y)+lift
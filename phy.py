def PlanePhy(self,wingarea,liftc, dragc, fluidDensity):
  fluidDensity = 1.225 #si units
  drag = fluidDensity*dragc*(self.vel.magnitude_squared()),wingarea/2
  lift =  liftc*fluidDensity*(self.vel.magnitude_squared())*wingarea/2
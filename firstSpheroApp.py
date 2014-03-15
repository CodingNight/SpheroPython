import sphero
from time import sleep
from random import random

ourSphero = sphero.Sphero()
ourSphero.connect()
sleep(1)

#initiation , set to white, define list
ourSphero.set_rgb(250,250,250)
heading = 0

color = [0,0,0]

def switchColor(color):
  return [round(random()*255),color[0],color[1]]

def switchHeading(heading):
  heading += 30
  return heading % 360

#
for i in range(1,1000):
  ourSphero.roll(50,heading)
  for j in range(1,3):
    sleep(0.02)
    ourSphero.set_rgb(color[0],color[1],color[2])
    color = switchColor(color)
  heading = switchHeading(heading)
  print i/10
  
sphero.roll(0,0)

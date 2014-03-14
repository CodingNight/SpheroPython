import sphero
from time import sleep

ourSphero = sphero.Sphero()
ourSphero.connect()
sleep(0.5)
ourSphero.set_rgb(0,0,0)

heading = 0
color = [255,0,0]

def switchcolor(color):
  return [color[2],color[0],color[1]]

def switchheading(heading):
  heading += 90
  return heading % 360

for i in range(1,10):
  ourSphero.roll(50,heading,10)
  for j in range(1,3):
    sleep(1)
    ourSphero.set_rgb(color[0],color[1],color[2])
    color = switchcolor(color)
  heading = switchheading(heading)
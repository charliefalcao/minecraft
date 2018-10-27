from mcpi.minecraft import Minecraft
from mcpi.block import *
from block_names import *
import random

import time

mc = Minecraft.create()

x_origin,y_origin,z_origin=mc.player.getPos()

generations = 0

for times in range(generations):
    size = int(random.uniform(1,15))
    x_start = int(x_origin - size / 2)
    z_start = int(z_origin - size / 2)
    for i in range(size):
        for dz in range(size):
            x = x_start + i
            z = z_start + dz
            y = mc.getHeight(x, z) - 1
            mc.setBlocks(x,y,z,x,y-1,z,tbAir())
#            time.sleep(0.00005)

generations = 1000

size = 100
depth = 4
x_hole = 20
z_hole = 20
for times in range(generations):
    x = x_origin + random.uniform(-size/2,size/2)
    z = z_origin + random.uniform(-size/2,size/2)
    y = mc.getHeight(x, z) - 1
    mc.setBlocks(x,y,z,x+x_hole,y-depth,z+z_hole,tbAir())
   # mc.postToChat(dx)
#            time.sleep(0.00005)

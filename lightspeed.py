from mcpi.minecraft import Minecraft
from mcpi.block import *
from block_names import *
import random

import time

mc = Minecraft.create()

x_origin,y_origin,z_origin=mc.player.getPos()

jumps = 80
step =7
time_step = 2
for i in range(jumps):
    x = x_origin + i*step
    z = z_origin + i*step
    y = mc.getHeight(x, z) + 40
    mc.player.setPos(x, y, z)
    time.sleep(0.4)


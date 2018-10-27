from mcpi.minecraft import Minecraft
from block_names import *
import random

import time

mc = Minecraft.create()

x_origin,y_origin,z_origin=mc.player.getTilePos()

quanti = 1000
for i in range(quanti):
    x_nulla,y_nulla,z_nulla = (x_origin + random.uniform(-100, 100) , y_origin+random.uniform(-100, 100) , z_origin+random.uniform(-100, 100) )
    width, height, length = (20,20,20)
    mc.setBlocks(x_nulla,y_nulla,z_nulla,x_nulla+width,y_nulla+height,z_nulla+length,tbAir(), 1)
    time.sleep(0.1)

from mcpi.minecraft import Minecraft
from mcpi.block import *
from block_names import *
import random

import time

mc = Minecraft.create()

x_origin,y_origin,z_origin=mc.player.getPos()

generations = 10000

size = 200
depth = 1
x_w = 1
z_w = 1
for times in range(generations):
    x = x_origin + random.uniform(-size/2,size/2)
    z = z_origin + random.uniform(-size/2,size/2)
    time.sleep(1)
    for i in range(x_w):
        for j in range(z_w):
            x_block = x + i
            z_block = z + j
            y_block = mc.getHeight(x_block, z_block)
            mc.setBlock(x_block,y_block,z_block,WATER.id)
    # mc.postToChat(dx)
#            time.sleep(0.00005)

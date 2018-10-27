from mcpi.minecraft import Minecraft
from mcpi.block import *
from block_names import *
import random

import time

mc = Minecraft.create()

x_origin,y_origin,z_origin=mc.player.getTilePos()

layers = 5
size = 10
for j in range(layers):
    y = y_origin - j
    for i in range(size):
        x = x_origin - (size - 1) / 2 + i
        for k in range(size):
            z = z_origin - (size - 1) / 2 + k
            mc.setBlock(x,y,z,AIR.id)
        

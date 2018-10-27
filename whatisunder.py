from mcpi.minecraft import Minecraft
from mcpi.block import *
from block_names import *
import random

import time

mc = Minecraft.create()

x_origin,y_origin,z_origin=mc.player.getTilePos()

blocks_found = []
coordinates = []

size = 2
depth = 200
for j in range(depth):
    y = y_origin - j
    for i in range(size):
        x = x_origin - (size - 1) / 2 + i
        for k in range(size):
            z = z_origin - (size - 1) / 2 + k
            block_type = mc.getBlock(x,y,z)
            if(not block_type in blocks_found):
                blocks_found.append(block_type)
                coordinates.append((x,y,z))
            

while True:
    time.sleep(5)
    mc.postToChat("Found: ")
    for i in range(len(coordinates)):
        coords = coordinates[i]
        mc.postToChat(str(blocks_found[i]) + "," + str(coords[0]) + "," + str(coords[1]) + "," + str(coords[2]) )
        

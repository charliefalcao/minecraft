from mcpi.minecraft import Minecraft
from mcpi.block import *
from block_names import *
import random

import time

mc = Minecraft.create()

x_origin,y_origin,z_origin=mc.player.getTilePos()

blocks_found = []
coordinates = []

size = 5
for i in range(size):
    x = x_origin - (size - 1) / 2 + i
    for j in range(size):
        y = y_origin - (size - 1) / 2 + j
        for k in range(size):
            z = z_origin - (size - 1) / 2 + k
            block_type = mc.getBlock(x,y,z)
            if(not block_type in blocks_found):
                #mc.postToChat("BlockType: " + str(block_type))
                blocks_found.append(block_type)
                coordinates.append((x,y,z))
                #mc.postToChat("Pos: " + str(x) + "," + str(y) + "," + str(z))

mc.postToChat("Found: ")
for i in range(len(coordinates)):
    coords = coordinates[i]
    mc.postToChat(str(blocks_found[i]) + "," + str(coords[0]) + "," + str(coords[1]) + "," + str(coords[2]) )
        

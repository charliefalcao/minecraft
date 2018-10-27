from mcpi.minecraft import Minecraft
from mcpi.block import *
from block_names import *
import random

import time

mc = Minecraft.create()

x_origin,y_origin,z_origin=mc.player.getTilePos()

blocks_found = []
coordinates = []
for i in range(2x`000):
    step = i*250
    x = x_origin+step
    y = y_origin 
    z = z_origin
    block_type = mc.getBlock(x,y,z)
    if(not block_type in blocks_found):
        mc.postToChat("BlockType: " + str(block_type))
        blocks_found.append(block_type)
        coordinates.append((x,y,z))
        mc.postToChat("Pos: " + str(x) + "," + str(y) + "," + str(z))
    elif(i%50==0):
        mc.postToChat("Distanza: " + str(step))
        mc.postToChat("Found: ")
        for i in range(len(coordinates)):
            coords = coordinates[i]
            mc.postToChat(str(blocks_found[i]) + "," + str(coords[0]) + "," + str(coords[1]) + "," + str(coords[2]) )
        

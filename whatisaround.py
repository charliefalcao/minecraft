from mcpi.minecraft import Minecraft
from mcpi.block import *
from block_names import *
import random
import math

import time

mc = Minecraft.create()

x_origin,y_origin,z_origin=mc.player.getTilePos()

def debugBlock(block_type, coords) :
    mc.postToChat(str(block_type) + "," + str(coords[0]) + "," + str(coords[1]) + "," + str(coords[2]) )

blocks_found = []
coordinates = []
dalpha = 0.1
depth = 1
length = 10000
d_depth = 0.01
for i in range(length):
    rho = 2 * i
    x = x_origin + rho * math.cos(i*dalpha)
    z = z_origin + rho * math.sin(i*dalpha)
    depth = i * d_depth
    y = mc.getHeight(x,z) - depth
    block_type = mc.getBlock(x,y,z)
    if(not block_type in blocks_found):       
        mc.postToChat("New Block")
        debugBlock(block_type, (x,y,z))
        blocks_found.append(block_type)
        coordinates.append((x,y,z))
    elif(i%50==0):
        mc.postToChat("Blocks")
        for j in range(len(coordinates)):
            debugBlock(blocks_found[j], coordinates[j])
        mc.postToChat("i = " + str(i))
        mc.postToChat("This block")
        debugBlock(block_type, (x,y,z))
            
while True:
    time.sleep(10)
    mc.postToChat("Final List")
    for i in range(len(coordinates)):
        debugBlock(blocks_found[i], coordinates[i])
       

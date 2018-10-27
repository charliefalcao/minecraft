from mcpi.minecraft import Minecraft
from mcpi.vec3 import *
from block_names import *
from mcpi.block import *

import time

mc = Minecraft.create()

distance = 3

for i in range(200):
    time.sleep(4)
    x_origin,y_origin,z_origin=mc.player.getTilePos()
    v_origin = Vec3(x_origin,y_origin, z_origin)
    direction = mc.player.getDirection()
    v_tnt =  direction
    v_tnt *= distance
    v_tnt += v_origin
    mc.setBlock(int(v_tnt.x),int(v_tnt.y),int(v_tnt.z),i, 1)
    mc.postToChat("BlockType: " + str(i))

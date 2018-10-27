from mcpi.minecraft import Minecraft
from mcpi.vec3 import *
from block_names import *
from mcpi.block import *

import time

mc = Minecraft.create()

x_origin,y_origin,z_origin=mc.player.getTilePos()

v_origin = Vec3(x_origin,y_origin, z_origin)
##mc.postToChat("Origin: ")
##mc.postToChat( v_origin)

direction = mc.player.getDirection()
##mc.postToChat("Direction: ")
##mc.postToChat( direction)

distance = 8

v_tnt =  direction
v_tnt *= distance
v_tnt += v_origin
##mc.postToChat("vtnt: ")
##mc.postToChat( v_tnt.x)

tetto = 4
mc.setBlocks(int(v_tnt.x)-2,int(v_tnt.y)+1,int(v_tnt.z)-2,int(v_tnt.x)+2,int(v_tnt.y)+tetto,int(v_tnt.z)+2,STONE.id,1)
mc.setBlocks(int(v_tnt.x),int(v_tnt.y)+1,int(v_tnt.z),int(v_tnt.x),int(v_tnt.y)+tetto,int(v_tnt.z),AIR.id,1)
mc.setBlocks(int(v_tnt.x)-2,int(v_tnt.y)-1,int(v_tnt.z)-2,int(v_tnt.x)+2,int(v_tnt.y),int(v_tnt.z)+2,STONE.id,1)
mc.setBlock(int(v_tnt.x),int(v_tnt.y)+1,int(v_tnt.z),TORCH_REDSTONE.id,1)
mc.setBlock(int(v_tnt.x),int(v_tnt.y),int(v_tnt.z),TNT.id, 1)
#mc.setBlock(int(v_tnt.x),int(v_tnt.y)+tetto,int(v_tnt.z),WATER.id, 1)
mc.setBlock(int(v_tnt.x),int(v_tnt.y)+3,int(v_tnt.z),TNT.id, 1)


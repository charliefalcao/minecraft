from mcpi.minecraft import Minecraft
from mcpi.block import *
from block_names import *
import random

import time

mc = Minecraft.create()

x_origin,y_origin,z_origin=mc.player.getTilePos()

##time.sleep(4)
##for level in range(7):
##    mc.setBlock(x_origin,y_origin,z_origin,WATER_STATIONARY.id, level)
##    time.sleep(2)
##    
##mc.setBlock(x_origin,y_origin,z_origin,AIR.id)

time.sleep(2)
mc.setBlock(x_origin+3,y_origin+100,z_origin,WATER_FLOWING.id)
#time.sleep(5)
#mc.setBlock(x_origin+3,y_origin,z_origin,AIR.id)

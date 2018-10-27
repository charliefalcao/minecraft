from mcpi.minecraft import Minecraft
from block_names import *

import time

mc = Minecraft.create()

x_origin,y_origin,z_origin=mc.player.getTilePos()

x_block,y_block,z_block = (x_origin + 5, y_origin+3, z_origin)

#for i in range(10):
# for i in range(10):
#    time.sleep(0.5)
#    mc.setBlock(x_block,y_block,z_block,i)
#    mc.postToChat("Blocco numero: " + str(i))

time.sleep(2)
mc.setBlock(x_block,y_block,z_block,tbMelon())
time.sleep(2)
mc.setBlock(x_block,y_block,z_block,tbAir())
time.sleep(2)
mc.setBlock(x_block,y_block,z_block,tbMelon())

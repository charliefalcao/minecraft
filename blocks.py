from mcpi.minecraft import Minecraft
from block_names import *

import time

mc = Minecraft.create()

x_origin,y_origin,z_origin=mc.player.getTilePos()

x_block,y_block,z_block = (x_origin + 5, y_origin+3, z_origin)

##durata = 20
##
##for i in range(durata):
##    time.sleep(0.8)
##    mc.setBlock(x_block,y_block,z_block,i)
##    mc.postToChat("Blocco numero: " + str(i))
##
##time.sleep(2)
##mc.setBlock(x_block,y_block,z_block,tbMelon())
##time.sleep(2)
##mc.setBlock(x_block,y_block,z_block,tbAir())
##time.sleep(2)
##mc.setBlock(x_block,y_block,z_block,tbLava())
##time.sleep(2)

x_blocks,y_blocks,z_blocks = (x_origin + 10, y_origin+3, z_origin)
width, height, length = (10,5,6)
mc.setBlocks(x_blocks,y_blocks,z_blocks,x_blocks+width,y_blocks+height,z_blocks+length,tbCobblestone())

x_blocks,y_blocks,z_blocks = (x_origin + 30, y_origin+3, z_origin)
width, height, length = (10,5,6)
mc.setBlocks(x_blocks,y_blocks,z_blocks,x_blocks+width,y_blocks+height,z_blocks+length,tbCobblestone())
mc.setBlocks(x_blocks+1,y_blocks+1,z_blocks+1,x_blocks+width-1,y_blocks+height-1,z_blocks-1+length,tbAir())
mc.setBlocks(x_blocks + 1,y_blocks,z_blocks +1,x_blocks+width - 1,y_blocks,z_blocks-1+length,tbAir())
mc.setBlocks(x_blocks+width/2,y_blocks,z_blocks,x_blocks+width/2+1,y_blocks+height/2,z_blocks,tbAir())

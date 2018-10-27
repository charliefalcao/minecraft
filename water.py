from mcpi.minecraft import Minecraft
from mcpi.block import *
from block_names import *
import random

import time

mc = Minecraft.create()

x_origin,y_origin,z_origin=mc.player.getTilePos()

x_w,y_w,z_w = (x_origin + 1,y_origin,z_origin)
width, height, length = (1,1,1)
mc.setBlocks(x_w,y_w,z_w,x_w+width,y_w+height,z_w+length,WATER.id, 1)
mc.setBlocks(x_w+10,y_w,z_w,x_w+10 + width,y_w+height,z_w+length,WATER_FLOWING.id, 1)
mc.setBlocks(x_w+20,y_w,z_w,x_w+20+width,y_w+height,z_w+length,WATER_STATIONARY.id, 1)


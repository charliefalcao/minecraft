from mcpi.minecraft import Minecraft
from mcpi.block import *
from block_names import *
import random

import time

mc = Minecraft.create()

x_origin,y_origin,z_origin=mc.player.getTilePos()

###mc.player.setTilePos(70365, 6, 261)
###sandstone
##mc.player.setTilePos(226, 100, 53)

#random teleport
max_l = 3000
x_random = random.uniform(-max_l, max_l)
z_random = random.uniform(-max_l, max_l)
y_random = mc.getHeight(x_random, z_random) + 40

mc.player.setTilePos(x_random, y_random, z_random)

mc.postToChat(mc.player.getTilePos())


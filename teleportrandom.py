from mcpi.minecraft import Minecraft
from mcpi.block import *
from block_names import *
import random

import time

def teleport():
    mc = Minecraft.create()

    #random teleport
    max_l = 3000
    x_random = random.uniform(-max_l, max_l)
    z_random = random.uniform(-max_l, max_l)
    y_random = mc.getHeight(x_random, z_random) + 40

    mc.player.setTilePos(x_random, y_random, z_random)

    mc.postToChat(mc.player.getTilePos())


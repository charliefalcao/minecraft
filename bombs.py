from mcpi.minecraft import Minecraft
from mcpi.vec3 import *
from block_names import *
from mcpi.block import *

import time

def bomba(potenza) :

    normalised_potenza = potenza / 0.03
    if(normalised_potenza <= 0): return
    if(normalised_potenza >= 1): normalised_potenza = 1

    potenza_max = 10
    potenza = int(normalised_potenza * potenza_max)
    
    mc = Minecraft.create()
    mc.postToChat("Bomba potenza: " + str(int(10 * normalised_potenza)))

    x_origin,y_origin,z_origin=mc.player.getTilePos()
    v_origin = Vec3(x_origin,y_origin, z_origin)
    direction = mc.player.getDirection()

    distance = 6 * potenza
    v_tnt =  direction
    v_tnt *= distance
    v_tnt += v_origin

    floors = 3
    mc.setBlocks(v_tnt.x - potenza,v_tnt.y+1,v_tnt.z-potenza,v_tnt.x+potenza,v_tnt.y+1,v_tnt.z+potenza,WOOD_PLANKS.id)
    mc.setBlocks(v_tnt.x - potenza,v_tnt.y,v_tnt.z - potenza,v_tnt.x + potenza,v_tnt.y-floors,v_tnt.z + potenza,TNT.id, 1)
    for row in range(potenza) :
        row_air = v_tnt.x - potenza + 2*row + 1
        mc.setBlocks(row_air,v_tnt.y+1,v_tnt.z - potenza,row_air,v_tnt.y + 1,v_tnt.z + potenza,AIR.id, 1)
        mc.setBlocks(row_air,v_tnt.y+1,v_tnt.z - potenza,row_air,v_tnt.y + 1,v_tnt.z + potenza,TORCH_REDSTONE.id, 1)

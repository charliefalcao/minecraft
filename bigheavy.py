from mcpi.minecraft import Minecraft
from mcpi.vec3 import *
from block_names import *
from mcpi.block import *

import time

mc = Minecraft.create()

def big_heavy(size) :

    normalised_size = size / 0.03
    if(normalised_size <=0): return
    if(normalised_size >= 1): normalised_size = 1

    dx_max = 50
    dx = normalised_size * dx_max
    mc.postToChat("Piramide grandezza: " + str(int(normalised_size * 10)))

        
    distance = normalised_size * 100
    lx = dx
    lz = dx

    x_origin,y_origin,z_origin=mc.player.getTilePos()
    
    v_origin = Vec3(x_origin,y_origin, z_origin) 
    v_tnt = mc.player.getDirection()
    v_tnt *= distance
    v_tnt += v_origin
    
    min_height = y_origin

    num_x = 2 * lx + 1
    num_z = 2 * lz + 1
    num_search = 5
    for i in range(num_search):
        x = v_tnt.x - lx + 2 * i * lx / (num_search - 1)
        for j in range(num_search):
            z = v_tnt.z - lz + 2 * j * lz / (num_search - 1)
            y = mc.getHeight(x,z)
            if(y < min_height):
                min_height = y

    floors_max = 150
    floors = int(normalised_size * floors_max)
    if floors == 0: return
    if(min_height + floors > 256):
        floors = 256 - min_height

    d1_over_n = 1./(floors - 1.)
    for f in range(floors):
        dx = (floors - f) * lx * d1_over_n
        dz = (floors - f) * lz * d1_over_n
        num_x = 2 * int(dx) + 1
        num_z = 2 * int(dz) + 1
        for i in range(num_x):
            x = v_tnt.x - dx + i
            for j in range(num_z):
                z = v_tnt.z - dz + j
#                y = mc.getHeight(x,z)
                y = min_height + f
                mc.setBlock(x,y,z,SAND.id)
    

#big_heavy(1)

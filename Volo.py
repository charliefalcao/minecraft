from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()
x=0
dx=0
z=0
dz=10
atterraggio = 1
fattore_atterraggio = 0.95
lunghezza_tempo = 100
for i in range(lunghezza_tempo):
    time.sleep(0.3)
    y = mc.getHeight(x, z)
    atterraggio *= fattore_atterraggio
    mc.player.setTilePos(x, y + 100 * atterraggio, z)
    x=x+dx
    z+=dz

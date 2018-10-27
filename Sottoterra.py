from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

y=1000
prev_block_type = -1
for i in range(1000):
    time.sleep(0.25)
    block_type = mc.getBlock(0, y, 0)
    if(block_type != 0) :
        mc.player.setTilePos(0, y, 0)
    y = mc.player.getTilePos().y - 1
    if(prev_block_type != block_type):
        mc.postToChat("Block type: " + str(block_type))
        prev_block_type = block_type
    

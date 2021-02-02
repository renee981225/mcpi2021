from mcpi.minecraft import Minecraft
mc=Minecraft.create()


while True:
    x,y,z=mc.player.getTilePos()
    mc.postToChat('X:'+str(x)+'Y:'+str(y)+'Z:'+str(z))
    
    
x,y,z=mc.player.getTilePos()    
mc.setBlock(x,y,z,46)
mc.setBlock(x,y+1,z+1,46)
mc.setBlock(x,y+2,z+2,46)
mc.setBlock(x,y+3,z+3,46)
mc.setBlock(x,y+4,z+4,46)
mc.setBlock(x,y+5,z+5,46)
mc.setBlock(x,y+6,z+6,46)
mc.setBlock(x,y+7,z+7,46)
mc.setBlock(x,y+9,z+8,46)
mc.setBlock(x,y+10,z+8,46)
mc.setBlock(x,y+11,z+8,46)
mc.setBlock(x,y+12,z+8,46)
mc.setBlock(x,y+13,z+8,46)
mc.setBlock(x,y+14,z+8,46)
mc.setBlock(x,y+15,z+8,46)



x,y,z=mc.player.getTilePos()

mc.setBlock(x+1,y,z+1,46)
mc.setBlock(x-1,y,z+1,46)
mc.setBlock(x,y,z-1,46)
mc.setBlock(x,y,z+1,46)
mc.setBlock(x+1,y,z+1,46)
mc.setBlock(x-1,y,z-1,46)
mc.setBlock(x-1,y,z,46)
mc.setBlock(x+1,y,z,46)
mc.setBlock(x+1,y,z-1,46)

x,y,z=mc.player.getTilePos()
mc.setBlocks(x+100,y,z+100,x-100,y,z-100,46)


import random
import time   
x,y,z=mc.player.getTilePos()

while True:
     r=random.randrange(0,16)
     mc.setBlocks(x+5,y,z+5,x-5,y,z-5,r)
     time.sleep(0.5)

    


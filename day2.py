from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x,y,z,= mc.player.getTilePos()
mc.setBlocks(x,y,z,x+12,y+12,z+12,219)
mc.setBlocks(x+1,y+1,z+1,x+11,y+11,z+11,0)



import  time

while True:
    x,y,z,=mc.player.getTilePos()
    mc.setBlock(x,y,z,76)
    time.sleep(0.5)
    
    
    
    
    

    

import  time

while True:
    x,y,z,=mc.player.getTilePos()
    mc.setBlock(x,y,z,8)
    mc.setBlock(x,y-1,z,19)
    time.sleep(10)
    
    
    
while True:
    x,y,z,=mc.player.getTilePos()
    a=mc.getBlock(x+1,y-1,z)
    b=mc.getBlock(x-1,y-1,z)
    c=mc.getBlock(x,y-1,z+1)
    d=mc.getBlock(x,y-1,z-1)
    
    if a==8 or a==9 or b==8 or b==9 or c==8 or c==9 or d==8 or d==9: 
        mc.setBlocks(x-1,y-1,z-1,x+1,y-1,z+1,57)
    
    
x,y,z=mc.player.getTilePos()

a=0
while a<5:
    mc.setBlocks(x+10,y-1,z,x-5,y-5,z,19)
    z=z+5
    a=a+1
    
x,y,z=mc.player.getTilePos()
a=int(input('哈囉你好嗎?'))
mc.setBlock(x,y,z,a)



name=input('enter your name:')
message=input('enter your message:')
mc.postToChat('<'+name+'>'+message)

x,y,z=mc.player.getTilePos()
mc.setSign(x,y,z,68,0,'123123','456456','789789')





























    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
from mcpi.minecraft import Minecraft
mc=Minecraft.create()

import random
import time

while True:
    x,y,z=mc.player.getTilePos()
    x=x+random.randrange(-10,10)
    y=y+30
    z=z+random.randrange(-10,10)
    
    mc.spawnEntity(x,y,z,93)
    time.sleep(0.2)

    
    
    
def plantTree(x,y,z):
    mc.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,95)
    mc.setBlocks(x,y,z,x,y+4,z,191)
    



x,y,z=mc.player.getTilePos()

for i in range(8):
    for j in range(8):
        for k in range(6):
            plantTree(x+i*5,y+j*i,z+k*i)
        
        
        
        
        
def buildPyramid(x,y,z): 
    base=20
    height=(base//2)+1
    
    for i in range(height):
        x1=x+i
        y1=y+i
        z1=z+i
        
        x2=x+base-i
        
        z2=z+base-i
        
        mc.setBlocks(x1,y1,z1,x2,y1,z2,24)
        
x,y,z=mc.player.getTilePos()
buildPyramid(x,y,z)        
        
        


line1=[]
line2=[]
line3=[]

for i in range(1,4):
    line1.append(1*i) 

for i in range(1,4):
    line2.append(2*i)

for i in range(1,4):
    line3.append(3*i) 

    
x,y,z=mc.player.getTilePos()
mc.setSign(x,y,z,63,0,str(line1),str(line2),str(line3))        
        
        
        
x,y,z=mc.player.getTilePos()

number=1

for i in range(8):
    for j  in range(number):  
        mc.spawnEntity(x,y,z,60)
        
        
    number=number*2
    mc.postToChat("11111"+str(number)+"個東西")
        
        
import time    
while True:
    mc.executeCommand('time add 50')
    time.sleep(0.01)
        
        
        
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


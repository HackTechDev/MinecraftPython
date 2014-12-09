import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()

while True:
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    
    # Display position
    #print x, y, z

    time.sleep(2)
    
    if x >= 343.300 and y <= 344.700 and z <= -301.300 and z >= -302.700 and y == 4:
        print "Active action"
        mc.postToChat("Active action")

import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import os
import sys
import twitter

consumer_key = ''
consumer_secret = ''
access_token_key = ''
access_token_secret = ''

api = twitter.Api(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token_key=access_token_key,
    access_token_secret=access_token_secret
)

if __name__ == "__main__":

    time.sleep(5)
    world = minecraft.Minecraft.create()

    print "Minecraft"
    world.postToChat("Bienvenue dans le monde Minecraft !")

    time.sleep(2)

    end = False

    playerPos = world.player.getPos()
    world.postToChat("Position : x=" + str(playerPos.x) + ", y=" + str(playerPos.y) + ", z=" + str(playerPos.z))

    while(end == False):
        timeline = api.GetUserTimeline(screen_name='Nekrofage666', exclude_replies=True)
        print timeline[0].text
        world.postToChat(timeline[0].text.encode('utf-8'))
        time.sleep(10)
      

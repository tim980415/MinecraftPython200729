# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:11:34 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time,random
while True:
    pos=mc.player.getPos()
    x=pos.x+random.uniform(-20,21)
    z=pos.x+random.uniform(-20,21)
    y=pos.y+100
    mc.spawnEntity(x,y,z,93)
    
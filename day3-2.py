# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 10:41:16 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
while True:
    hits=mc.events.pollProjectileHits()
    if len(hits)>0:
        
        block=hits[0]
        x,y,z=block.pos.x,block.pos.y,block.pos.z
        a=mc.getBlock(x,y,z)
        mc.createExplosion(x,y,z,power=500)
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 15:00:43 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
 
x,y,z = mc.player.getTilePos()
base = 100
height = (base//2)+1
 
for i in range(height):
    x1 = x + i
    y1 = y + i
    z1 = z + i
    
    x2 = x + base - i
    #y與y2相同
    z2 = z + base - i
    mc.setBlocks(x1, y1, z1, x2, y1, z2, 46)
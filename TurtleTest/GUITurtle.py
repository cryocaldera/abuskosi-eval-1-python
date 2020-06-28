# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 19:04:33 2020

@author: sritt
"""
import turtle as tu

tu.bgcolor('black')
tu.color('yellow')

for i in range(0, 6):
    tu.forward(30)
    tu.left(60)
    tu.forward(30)

tu.Screen().exitonclick()

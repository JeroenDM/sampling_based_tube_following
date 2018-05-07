#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from ppr.robot import RobotManyDofs
from ppr.path import TrajectoryPt, TolerancedNumber
from ppr.geometry import Rectangle

# ROBOT
robot1 = RobotManyDofs(8, link_length=1)
robot1.set_joint_limits([(-np.pi / 2, np.pi / 2)] * 8)

# PATH
#dx    = TolerancedNumber(2, 0.3, 0.8, samples=3)
dx    = np.ones(5) * 5
dy    = np.linspace(1.3, 2.5, 5)
angle = TolerancedNumber(0.0, -np.pi/2, np.pi/2, samples=10)
path1 = [TrajectoryPt([dx[i], dy[i], angle]) for i in range(5)]

# COLLISION SCENE
sc1 = []
sc1.append(Rectangle(0, -1, 5, 0.2, 0)) # horizontal lower
sc1.append(Rectangle(0, 3, 5, 0.2, 0)) # horizontal upper
sc1.append(Rectangle(1, -1, 0.2, 2.5, 0)) # vertical left
sc1.append(Rectangle(2.5, 1, 0.2, 2, 0)) # vertical middle
sc1.append(Rectangle(4, -1, 0.2, 2.5, 0)) # vertical right
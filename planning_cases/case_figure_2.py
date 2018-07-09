# -*- coding: utf-8 -*-
import numpy as np
from ppr.robot import Robot_2P3R
from ppr.path import TrajectoryPt, TolerancedNumber
from ppr.geometry import Rectangle

#%%============================================================================
# Define Robot and scene used to illustrate a path split in segments
#==============================================================================
# ROBOT
robot1 = Robot_2P3R([6, 0.9, 1.2, 1, 1])
robot1.set_joint_limits([(0, 6), (0.2, 0.9)])
robot1.ik_samples = [40, 3]

# PATH
x     = np.linspace(1, 5, 15)
dy    = TolerancedNumber(3.8, 3.6, 4.0, samples=4)
angle = TolerancedNumber(0.0, 0, np.pi, samples=20)
path1 = [TrajectoryPt([xi, dy, angle]) for xi in x]

# COLLISION SCENE
sc1 = []
sc1.append(Rectangle(2.5, 2, 1, 1, 0))


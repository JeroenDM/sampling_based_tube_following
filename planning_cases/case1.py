#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import path
path.append(r"/home/jeroen/Documents/gitlab/planar_python_robotics")

import numpy as np
from ppr.robot import Robot_2P3R
from ppr.path import TrajectoryPt, TolerancedNumber
from ppr.geometry import Rectangle

# ROBOT
robot1 = Robot_2P3R([4, 0.9, 2, 1.2, 1])
robot1.set_joint_limits([(2.0, 3.0), (0.0, 0.9)])
#robot1.ik_samples = [10, 9]

# PATH
dx    = TolerancedNumber(0.5, 0.3, 0.8, samples=5)
dy    = np.linspace(2, 2.5, 5)
angle = TolerancedNumber(0.0, -np.pi, 0, samples=32)
path1 = [TrajectoryPt([dx, yi, angle]) for yi in dy]

# COLLISION SCENE
sc1 = [Rectangle(1, 1, 1, 1.5, 0),
       Rectangle(3, 1, 1, 2.2, 0),
       Rectangle(0, 3.2, 4, 0.5, 0),
       Rectangle(0, 1, 0.2, 2.2, 0),
       Rectangle(0.2, 1, 0.8, 0.5, 0)]
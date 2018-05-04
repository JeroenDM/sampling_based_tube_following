#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Experiment 2 from paper
'Probabilistic Motion Planning for Redundant Robots
along Given End-Effector Paths'
Giuseppe Oriolo, Mauro Ottavi, Marilena Vendittelli
"""
from sys import path
path.append(r"/home/jeroen/Documents/gitlab/planar_python_robotics")

import numpy as np
from ppr.robot import RobotManyDofs
from ppr.path import TrajectoryPt, TolerancedNumber
from ppr.geometry import Rectangle

# ROBOT
robot1 = RobotManyDofs(6, link_length=2)
robot1.set_joint_limits([(-np.pi / 2, np.pi / 2)] * 6)
robot1.do_check_self_collision = True

# PATH line in gap
N = 5
G = 0.5
x = G / 2 * np.ones(N)
y = np.linspace(4, 6, N)
a = TolerancedNumber(0, 0, np.pi, samples=10)
path1 = [TrajectoryPt([x[i], y[i], a]) for i in range(N)]

# collision scene small gap width G
sc1 = []
sc1.append(Rectangle(-2, 4, 2, 4, 0))
sc1.append(Rectangle( G, 4, 2, 4, 0))
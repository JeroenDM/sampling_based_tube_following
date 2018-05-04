#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

from planning_cases import case1
from planning_cases import case2
from planning_cases import case3

# joint values to plot robots in nice positions
# based on the results from the path planning algorithms
q1 = [ 2.100,  0.756, -0.256,  1.530 , 0.863]
q2 = [-0.058,  0.565,  1.186,  2.198 , -1.017, -1.375]
q3 = [ 0.789,  0.443, -1.344,  -0.834,  1.122,  1.887, -2.059, -0.513]

# set font similar to the the latex file
plt.rc('font', family='serif')

# create 3 subplots for the 3 cases
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12,4))

# plot the robot, path and collision scene for the 3 cases
ax1.set_title("Case 1: 2P 3R robot", fontsize=24)
case1.robot1.plot(ax1, q1, 'k')
for tp in case1.path1: tp.plot(ax1, show_tolerance=False)
for r in case1.sc1: r.plot(ax1, 'grey')

ax2.set_title("Case 2: 6R robot", fontsize=24)
case2.robot1.plot(ax2, q2, 'k')
for tp in case2.path1: tp.plot(ax2, show_tolerance=False)
for r in case2.sc1: r.plot(ax2, 'grey')

ax3.set_title("Case 3: 8R robot", fontsize=24)
case3.robot1.plot(ax3, q3, 'k')
for tp in case3.path1: tp.plot(ax3, show_tolerance=False)
for r in case3.sc1: r.plot(ax3, 'grey')

# change some settings for all axes objects
for ax in [ax1, ax2, ax3]:
    ax.axis('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.plot(0, 0, '^k', markersize=10)

# fix spacing in between figures
fig.tight_layout()

# show and save figure
plt.show()
fig.savefig('figure/planning_cases.png')

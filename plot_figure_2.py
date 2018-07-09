#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

from planning_cases.case_figure_2 import robot1, sc1, path1
from ppr.sampling import cart_to_joint
from ppr.graph_pure_python import get_shortest_path_segments

#%%============================================================================
# Calculate a path that will consist of different segments
# the parameter 2 gives the maximum joint motion in between two
# trajectory points in radians
#==============================================================================
path_js = cart_to_joint(robot1, path1, check_collision=True, scene=sc1)
sol = get_shortest_path_segments(path_js, 2)

#%%============================================================================
# Create a plot from the solution
#==============================================================================
fig2, ax2 = plt.subplots()
ax2.axis('equal')
robot1.plot_path(ax2, sol['path'])
robot1.plot_path(ax2, sol['extra_segments'][0]['path'])
for r in sc1: r.plot(ax2, 'k')
for tp in path1: tp.plot(ax2, show_tolerance=False)
path1[-1].plot(ax2)

ax2.set_xlim([0.5, 5.5])
ax2.set_ylim([-0.5, 4.5])
ax2.set_xticks([])
ax2.set_yticks([])

fig2.savefig('figure/figure2.png')

plt.show()

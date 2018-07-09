#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import time
from ppr.path import TrajectoryPt, TolerancedNumber
from ppr.sampling import cart_to_joint, get_shortest_path


from planning_cases.case2 import robot1, sc1

robot1.ik_samples = [6, 6, 6] # 3 of the 6 joints redundant


def runner(num_path_points):
    # PATH line in gap
    N = num_path_points
    G = 0.5
    x = G / 2 * np.ones(N)
    y = np.linspace(4, 6, N)
    a = TolerancedNumber(0, 0, np.pi, samples=30)
    path1 = [TrajectoryPt([x[i], y[i], a]) for i in range(N)]
    
    start_time = time.time()
    
    path_js = cart_to_joint(robot1, path1, check_collision=True, scene=sc1)
    result = get_shortest_path(path_js)
    
    end_time = time.time()
    
    return result, (end_time - start_time)

#%%
solutions = []
times1 = []
for i in [5, 7, 9, 11, 13, 15]:
    temp1, temp2 = runner(i)
    solutions.append(temp1)
    times1.append(temp2)
    
times1 = np.array(times1)

#%%

fig, ax = plt.subplots()
ax.axis('equal')
robot1.plot_path(ax, solutions[-1]['path'])
for r in sc1: r.plot(ax, 'k')

#%%
n = [5, 7, 9, 11, 13, 15]

plt.figure()
plt.plot(n, times1, '.-')
plt.xlabel('Number of path points')
plt.ylabel('Computation time [s]')
plt.show()
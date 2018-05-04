#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


from planning_cases.case1 import robot1, path1, sc1
from utility import run_iterative_grid_refining

#%%============================================================================
# RUN Case 1 (in spyder IDE use ctrl + enter to run only this cell)
# for different grid sizes
#==============================================================================

## grid 1
robot1.ik_samples = [3, 5]
for tp in path1:
    tp.p[0].set_samples(4)
    tp.p[2].set_samples(10)

sol_1, total_time_1 = run_iterative_grid_refining(robot1, path1, sc1)
sol_1['samples'] = 3 * 5 * 4 * 10

## grid 2
robot1.ik_samples = [3, 5]
for tp in path1:
    tp.p[0].set_samples(5)
    tp.p[2].set_samples(20)

sol_2, total_time_2 = run_iterative_grid_refining(robot1, path1, sc1)
sol_2['samples'] = 3 * 5 * 5 * 10
    
## grid 3
robot1.ik_samples = [3, 5]
for tp in path1:
    tp.p[0].set_samples(5)
    tp.p[2].set_samples(35)

sol_3, total_time_3 = run_iterative_grid_refining(robot1, path1, sc1)
sol_3['samples'] = 3 * 5 * 5 * 35

#%%============================================================================
# Save results
#==============================================================================
np.save('data/iterative_grid_refining_case_1.npy', [sol_1, sol_2, sol_3])
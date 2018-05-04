#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

from planning_cases import case1
from planning_cases import case2
from planning_cases import case3
from utility import create_incremental_sampling_runner

#%%============================================================================
# Simulation setup
#==============================================================================

# maximum iterations the same for all cases
max_iters = 50

# test levels mininum joint solutions / path point
min_js_levels_1 = [1, 5, 10, 15, 20, 30, 40, 100, 200, 500]
min_js_levels_2 = [1, 5, 20, 50, 100, 200]
min_js_levels_3 = [1, 5, 10, 20, 50, 100]

# T-space and C-space sample increments
# aim for the same ratio used in the single runs
ti_1 = 18;  ci_1 = 10;  # ain for ratio (160/90)
ti_3 = 4;  ci_3 = 500; # aim for ratio (20 / 5**5) 
ti_2 = 10; ci_2 = 72;   # aim for ratio (30/6**3)

# create runner functions to execute simulations
run_1 = create_incremental_sampling_runner(case1.robot1, case1.path1, case1.sc1)
run_2 = create_incremental_sampling_runner(case2.robot1, case2.path1, case2.sc1)
run_3 = create_incremental_sampling_runner(case3.robot1, case3.path1, case3.sc1)

#%%============================================================================
# RUN Case 1 (in spyder IDE use ctrl + enter to run only this cell)
#==============================================================================
results_1 = {'cost': [], 'time': [], 'n_total': [], 'path': []}

for min_js in min_js_levels_1:
    # put settins in dict
    opts = {'max_iters': max_iters,
        'min_js': min_js,
        'js_inc': ti_1,
        'red_js_inc': ci_1,
        'ik_sampling_method': 'halton'}
    # run simulations
    res = run_1(opts)
    # add results to results_1 dict using the same keys
    for key in res:
        results_1[key].append(res[key])

#%%============================================================================
# RUN Case 2
#==============================================================================
results_2 = {'cost': [], 'time': [], 'n_total': [], 'path': []}

for min_js in min_js_levels_2:
    opts = {'max_iters': max_iters,
        'min_js': min_js,
        'js_inc': ti_2,
        'red_js_inc': ci_2,
        'ik_sampling_method': 'halton'}
    res = run_2(opts)
    for key in res:
        results_2[key].append(res[key])

#%%============================================================================
# RUN Case 3
#==============================================================================
results_3 = {'cost': [], 'time': [], 'n_total': [], 'path': []}

for min_js in min_js_levels_3:
    opts = {'max_iters': max_iters,
        'min_js': min_js,
        'js_inc': ti_3,
        'red_js_inc': ci_3,
        'ik_sampling_method': 'halton'}
    res = run_3(opts)
    for key in res:
        results_3[key].append(res[key])
        
#%%============================================================================
# Save results
#==============================================================================
#np.save('data/incremental_sampling_results_1.npy', results_1)
#np.save('data/incremental_sampling_results_2.npy', results_2)
#np.save('data/incremental_sampling_results_3.npy', results_3)
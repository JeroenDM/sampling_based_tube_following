#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

from planning_cases.case1 import robot1, path1, sc1
from utility import create_runner_raw

#%%============================================================================
# Simulation setup
#==============================================================================
# Repeatability for uniform random sampling
np.random.seed(42)

# Create custom runner to execute multiple fixed sampling runs
# where the case 1 specific path tolerances are used as input
def run_1(NC, NT1, NT2):
    res = {}
    
    robot1.ik_samples = [NC, NC]
    for tp in path1:
        tp.p[0].set_samples(NT1)
        tp.p[2].set_samples(NT2)
    
    # T-space and C-space increments for methods random and halton are
    # NT1 * NT2 and NC**2 respectively
    run = create_runner_raw(1, robot1, path1, sc1, NT1*NT2, NC**2)
    
    for m, nr in zip(methods, n_runs):
        r = run(m, num_runs=nr)
        res.update(r)
    return res

np.random.seed(42) # ensure repeatablility

# define methods, and the number of runs for each method
# on my computer (Intel® Core™ i7 2.90GHz) it takes +/- 1 min and 10 s
# using the 6 different resolutions settings defined below
# for a single run of the three methods
methods = ['grid', 'random', 'halton']
#n_runs = [2, 2, 2]
n_runs = [10, 10, 10]

# Define the different resolutions that will be used
# again we try to keep the ratio's for the different sample lists constants
ik_samples    = [1, 2,  4,  5, 10, 15]
x_samples     = [1, 1,  2,  3,  5,  8]
angle_samples = [3, 6, 12, 15, 30, 45]

# Other setting to you can use for shorter test runs
#ik_samples = [1, 2, 4, 5]
#x_samples = [1, 1, 2, 3]
#angle_samples = [3, 6, 12, 15]
#ik_samples = [10]
#x_samples = [5]
#angle_samples = [30]

# emtpy list / dict for results
#results = []
results = {'time_grid_1': [],
           'cost_grid_1': [],
           'sr_grid_1':   [],
           'all_times_grid_1': [],
           'samples_1': [],
           'time_random_1': [],
           'cost_random_1': [],
           'sr_random_1': [],
           'all_times_random_1': [],
           'time_halton_1': [],
           'cost_halton_1':[],
           'sr_halton_1': [],
           'all_times_halton_1': []}

#%%============================================================================
# RUN Case 1 (in spyder IDE use ctrl + enter to run only this cell)
#==============================================================================
for nc, ntx, nta in zip(ik_samples, x_samples, angle_samples):
    #results.append(run_1(nc, ntx, nta))
    res = run_1(nc, ntx, nta)
    for key in res:
        results[key].append(res[key])
print(results)

#%%============================================================================
# Save results
#==============================================================================
np.save('data/different_resolutions_case_1.npy', results)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

from planning_cases import case1
from planning_cases import case2
from planning_cases import case3
from utility import create_runner


#%%============================================================================
# Simulation setup
#==============================================================================
# Repeatability for uniform random sampling
np.random.seed(42)

# all sampling methods in this list will be tested for the three cases
methods = ['grid', 'random', 'halton']

# specify how many runs we should execute for each sampling method
# on my computer (Intel® Core™ i7 2.90GHz) it takes 1 minute to run
# all three cases for three sampling methods
# Running the [20, 20, 20] simulations of the paper takes +/- 20 minutes
n_runs = [1, 1, 1] # for paper results: [20, 20, 20]

# empty dictionary to save results
res = {}

# GRID SAMPLING settings
# ----------------------
# set resutotion for sampling inverse redundant joints
case1.robot1.ik_samples = [10, 9]   # 2 of the 5 joints redundant
case2.robot1.ik_samples = [6, 6, 6] # 3 of the 6 joints redundant
case3.robot1.ik_samples = [5] * 5   # 5 of the 8 joints redundant

# set resolution for path tolerance
for tp in case1.path1:
    tp.p[2].set_samples(5)
    tp.p[2].set_samples(32)
for tp in case2.path1: tp.p[2].set_samples(30)
for tp in case3.path1: tp.p[2].set_samples(20)

# HALTON and RANDOM settings
# -------------------------------------------------
# Set these to the same number of T-space and C-space samples as above
nt_1 = 5 * 32
nc_1 = 10 * 9
nt_2 = 30
nc_2 = 6 * 6 * 6
nt_3 = 20
nc_3 = 5 ** 5

# Create simulation runner with these settings
run_1 = create_runner(1, case1.robot1, case1.path1, case1.sc1, nt_1, nc_1)
run_2 = create_runner(2, case2.robot1, case2.path1, case2.sc1, nt_2, nc_2)
run_3 = create_runner(3, case3.robot1, case3.path1, case3.sc1, nt_3, nc_3)

#%%============================================================================
# RUN Case 1 (in spyder IDE use ctrl + enter to run only this cell)
#==============================================================================
print("Running Case 1 =======================================================")
for m, nr in zip(methods, n_runs):
    r = run_1(m, num_runs=nr)
    res.update(r)
print(res)

#%%============================================================================
# RUN Case 2
#==============================================================================
print("Running Case 2 =======================================================")
for m, nr in zip(methods, n_runs):
    r = run_2(m, num_runs=nr)
    res.update(r)
print(res)

#%%============================================================================
# RUN Case 3
#==============================================================================
print("Running Case 3 =======================================================")
for m, nr in zip(methods, n_runs):
    r = run_3(m, num_runs=nr)
    res.update(r)
print(res)

#%%============================================================================
# Write results to latex table
#==============================================================================
import numpy as np
from string import Template

# read template into string s
with open('table_1_template.txt', 'r') as tf:
    s = tf.readlines()
s = ''.join(s)
print(s)

s_new = Template(s).substitute(res)
print(s_new)

with open('table_1.tex', 'w') as file:
    file.write(s_new)

#%%============================================================================
# Timing computation time is not an exact process...
# Plot variation on timing to see if it is reasobable
#==============================================================================
fig, ax = plt.subplots(3, 3)
for i in range(3):
    ax[0, i].plot(res['all_times_grid_' + str(i+1)])
    ax[0, i].set_xticks([])
for i in range(3):
    ax[1, i].plot(res['all_times_random_' + str(i+1)])
    ax[1, i].set_xticks([])
for i in range(3):
    ax[2, i].plot(res['all_times_halton_' + str(i+1)])
    ax[2, i].set_xticks([])

plt.tight_layout()
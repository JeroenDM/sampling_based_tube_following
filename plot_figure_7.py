#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# load data
# (.item() is because it is put in a strange type of array when saving)
data_fix = np.load('data/different_resolutions_case_1.npy').item()
data_inc = np.load('data/incremental_sampling_results_1.npy').item()

# put data in variables for plotting
samples_fix = data_fix['samples_1']
time_fix    = data_fix['time_halton_1']
samples_inc = data_inc['n_total']
time_inc    = data_inc['time']

# don't use the last point of fixed sampling
# because there is no incremental data point to compare it with
samples_fix.pop(5)
time_fix.pop(5)

fig, ax = plt.subplots()
LW = 3; MS = 12; # linewidth and markersize
ax.plot(samples_inc, time_inc, '.-', color='k', lw=LW, ms=MS)
ax.plot(samples_fix, time_fix, '.--', color='gray', lw=LW, ms=MS)
ax.set_xlabel('# samples', fontsize=18)
#ax.set_ylim([0, 4])
ax.set_ylabel('Time [s]', fontsize=18)
ax.set_title('Case 1 (Halton sampling)', fontsize=20)

ax.legend(['Incremental', 'Fixed'], fontsize=18)
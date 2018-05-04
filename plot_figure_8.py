#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# load data
data = np.load('data/iterative_grid_refining_case_1.npy')

for d in data:
    print(d)

linestyles = ['-k', '--k', ':k']

LW=3;
fig, ax1 = plt.subplots(figsize=(7, 5))

legend_labels = []
for d, ls in zip(data, linestyles):
    ax1.plot(d['time'], d['length_all_iterations'], ls, lw=LW)
    legend_labels.append(d['samples'])

ax1.set_xlabel("Running time [s]", fontsize=18)
ax1.set_ylabel("Total path cost [rad]", fontsize=18)
ax1.set_ylim([0, 0.8])
ax1.tick_params(labelsize=12)
ax1.axhline(0.29, linestyle='-', color='grey')
ax1.legend(legend_labels, title='Samples / iteration', fontsize=16)
ax1.get_legend().get_title().set_fontsize(16)
ax1.text(0.1, 0.01, 'Horizontal line: single run 81000 samples \n (running time 19.7 s)', fontsize=14)
plt.show()

fig.savefig('figure/figure_8.png')
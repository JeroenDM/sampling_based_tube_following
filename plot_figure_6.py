#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# load data
# (.item() is because it is put in a strange type of array when saving)
data = np.load('data/different_resolutions_case_1.npy').item()

# put data in variables for plotting
samples = data['samples_1']
sr_grid = data['sr_grid_1']
sr_random= data['sr_random_1']
sr_halton = data['sr_halton_1']
cost_grid = data['cost_grid_1']
cost_random= data['cost_random_1']
cost_halton = data['cost_halton_1']

methods = ['Grid', 'Random', 'Halton']

plt.rc('font', family='serif')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
LW = 3; MS = 12; # linewidth and markersize
ax1.semilogx(samples, sr_grid, '.:', color='grey', lw=LW, ms=MS)
ax1.semilogx(samples, sr_random, '.-', color='gray', lw=LW, ms=MS)
ax1.semilogx(samples, sr_halton, '.--', color='k', lw=LW, ms=MS)
ax1.set_xlabel('# samples', fontsize=18)
ax1.set_yticks([0, 1])
#ax.set_yticklabels(['fail', 'success'])
ax1.set_ylabel('Success rate', fontsize=18)
ax1.legend(methods, fontsize=18)


ax2.semilogx(samples, cost_grid, '.:', color='grey', lw=LW, ms=MS)
ax2.semilogx(samples, cost_random, '.-', color='gray', lw=LW, ms=MS)
ax2.semilogx(samples, cost_halton, '.--', color='k', lw=LW, ms=MS)
ax2.set_xlabel('# samples', fontsize=18)
#ax2.set_ylim([0, 1.7])
#ax2.set_yticks([0, 1])
#ax.set_yticklabels(['fail', 'success'])
ax2.set_ylabel('Cost [rad]', fontsize=18)
#ax2.legend(methods, fontsize=18)

ax1.tick_params(labelsize=12)
ax2.tick_params(labelsize=12)

fig.suptitle("Case 1", y=1.05, fontsize=20)
plt.tight_layout()

plt.show()

fig.savefig('figure/figure_6.png')
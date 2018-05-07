#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge

from ppr.path import TrajectoryPt, TolerancedNumber

#%%============================================================================
# Modify plot function of trajectory point
# adapt the radius of the wedges
# this should probably be an optional parameter for the plot function
#==============================================================================
class ModifiedTP(TrajectoryPt):
    def plot(self, axes_handle, show_tolerance=True):
        """ Visualize the path on given axes
        
        Parameters
        ----------
        axes_handle : matplotlib.axes.Axes
        show_tolerance : bool
            If True, the range for a TolerancedNumber is showed.
            A bar for x or y position, A wedge for orientation tolerance.
            (default True)
        """
        pn = self.p_nominal
        axes_handle.plot(pn[0], pn[1], 'k*')
        if show_tolerance:
            if self.hasTolerance[0]:
                do = -self.p[0].l + pn[0]
                du =  self.p[0].u - pn[0]
                axes_handle.errorbar(pn[0], pn[1], xerr=[[do], [du]], color=(0.5, 0.5, 0.5))
            if self.hasTolerance[1]:
                do = -self.p[1].l + pn[1]
                du =  self.p[1].u - pn[1]
                axes_handle.errorbar(pn[0], pn[1], yerr=[[do], [du]], color=(0.5, 0.5, 0.5))
            if self.hasTolerance[2]:
                # scale radius relative to trajectory point position
                radius = (pn[0] + pn[1]) / 35
                do = self.p[2].l * 180 / np.pi
                du = self.p[2].u * 180 / np.pi
                arc = Wedge((pn[0], pn[1]), radius, do, du, facecolor=(0.5, 0.5, 0.5, 0.5))
                axes_handle.add_patch(arc)

#%%============================================================================
# Define the paths we will plot
#==============================================================================
R = 6 # factor to reduce the tolerancecs

# Original PATH 1
#----------------
dx    = np.linspace(3, 5, 10)
dy    = TolerancedNumber(1.0, 0.8, 1.2, samples=5)
angle = TolerancedNumber(0.0, -np.pi/2, np.pi/2, samples=10)
path1 = [ModifiedTP([xi, dy, angle]) for xi in dx]

# Path 2
#-------
# created based on an actual path plan
# but recreated here to focus on illustrating the concept
x2   = np.linspace(3, 5, 10)
y2 = [1.15, 1.10,    1,    1, 1, 1, 1, 0.95, 0.9, 0.85]
a2 = [-0.8, -0.6, -0.4, -0.2, 0, 0, 0,  0.3, 0.6,  0.8]

delta_y = 0.4 / R
delta_a = np.pi / R

dy = []
for yi in y2:
    dy.append(TolerancedNumber(yi, yi - delta_y, yi + delta_y))

da = []
for ai in a2:
    da.append(TolerancedNumber(ai, ai - delta_a, ai + delta_a))

path2 = [ModifiedTP([x2[i], dy[i], da[i]]) for i in range(10)]

#%%============================================================================
# Plot figure
#==============================================================================

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 4))

for tp in path1: tp.plot(ax1)
ax1.plot(x2, y2, 'k^', ms=8)
ax1.set_title('Original path points', fontsize=18)
ax1.set_xticklabels([])
ax1.set_ylabel('y-positoin', fontsize=14)

for tp in path2: tp.plot(ax2)
ax2.set_title('Reduced tolerances', fontsize=18)
ax2.set_xlabel('x-position', fontsize=14)
ax2.set_ylabel('y-position', fontsize=14)

fig.savefig('figure/figure4.png')

fig.tight_layout()
plt.show()
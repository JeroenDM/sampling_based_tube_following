#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Utility functions to run simulations with planning cases

For use of the ppr package:
 Point to where the planar_python_robotics packages lives, download from:
 https://gitlab.mech.kuleuven.be/u0100037/planar_python_robotics
 using the branch "May_3th_2018_backup_point"
"""
from sys import path
path.append(r"/home/jeroen/Documents/gitlab/planar_python_robotics")

import time
import numpy as np

from ppr.sampling import cart_to_joint, cart_to_joint_dynamic
from ppr.sampling import get_shortest_path, iterative_bfs

def create_runner(case_number, robot, path, scene, nt, nc):
    cn = '_' + str(case_number)
    def runner(method, num_runs=1):
        times = []
        costs = []
        failed = 0
        for i in range(num_runs):
            start_time = time.time()
            js = cart_to_joint(robot,
                               path,
                               check_collision=True,
                               scene=scene,
                               method=method,
                               N_cart=nt,
                               N_red_joints=nc)
            sol = get_shortest_path(js, method='dijkstra')
            run_time = time.time() - start_time
            
            if sol['success']:
                times.append(run_time)
                costs.append(sol['length'])
            else:
                failed += 1
                print("Failed at solving with method: " + method)
                print([len(qp) for qp in js])
        
        results = {}
        # TODO: only round result when actually putting them in the table
        results['time_' + method + cn] = '{:.2f}'.format(np.mean(times))
        results['cost_' + method + cn] = '{:.2f}'.format(np.mean(costs))
        success_rate = num_runs - failed
        results['sr_' + method + cn] = '{}/{}'.format(success_rate, num_runs)
        results['all_times_' + method + cn] = times
        #results['path_' + method] = sol['path']
        if method == 'grid':
            n_total = nt * np.prod(robot.ik_samples)
        else:
            n_total = nt * nc
        results['samples' + cn] = n_total
        #results['joint_solutions'] = js
        return results
    return runner

def create_runner_raw(case_number, robot, path, scene, nt, nc):
    cn = '_' + str(case_number) # used to tag results with case number
    n_path = len(path) # used to add the total number of samples to results
    def runner(method, num_runs=1):
        times = []
        costs = []
        failed = 0
        for i in range(num_runs):
            start_time = time.time()
            js = cart_to_joint(robot,
                               path,
                               check_collision=True,
                               scene=scene,
                               method=method,
                               N_cart=nt,
                               N_red_joints=nc)
            sol = get_shortest_path(js, method='dijkstra')
            run_time = time.time() - start_time
            
            if sol['success']:
                times.append(run_time)
                costs.append(sol['length'])
            else:
                failed += 1
                print("Failed at solving with method: " + method)
                print([len(qp) for qp in js])
        
        results = {}
        # TODO: only round result when actually putting them in the table
        results['time_' + method + cn] = np.mean(times)
        results['cost_' + method + cn] = np.mean(costs)
        success_runs = num_runs - failed
        results['sr_' + method + cn] = success_runs / num_runs
        results['all_times_' + method + cn] = times
        #results['path_' + method] = sol['path']
        results['samples' + cn] = nt * nc * n_path
        #results['joint_solutions'] = js
        return results
    return runner

def create_incremental_sampling_runner(robot, path, scene):
    def runner(options):
        start_time = time.time()
        js, info = cart_to_joint_dynamic(robot, path,
                                   check_collision=True,
                                   scene=scene,
                                   parameters=options,
                                   return_sample_info=True)
        sol = get_shortest_path(js)
        run_time = time.time() - start_time
        
        if sol['success']:
            res = {}
            res['path'] = sol['path']
            res['cost'] = sol['length']
            res['time'] = run_time
            res['n_total'] = info[2] # total number of samples
            return res
        else:
            print("failed to find solution for these options")
    
    return runner

def run_iterative_grid_refining(robot, path, scene):
    start_time = time.time()
    sol = iterative_bfs(robot, path, scene, tol=1e-6, red=3, max_iter=10)
    run_time = time.time() - start_time
    return sol, run_time
#!/usr/bin/python
# Reminder -- flush regularly

from basic_functions import * 
from tsp_algos import *
from ga import *

# Begin Main:
N, c, d = read_inp('problems/euc_100')

"""
print "Nearest Neighbour: \n"
t = greedy_tour(d, N)
print_tour(t, N)
print cost_tour(t, d, N)
"""

"""
print "\n\nSaving Heuristic: \n"
t = savings_heuristic(d, N)
print_tour(t, N)
print cost_tour(t, d, N)
"""

print "Genetic Algo: \n"
t = genetic_algo(d, N)
print_tour(t)
print cost_tour(t, d, N)
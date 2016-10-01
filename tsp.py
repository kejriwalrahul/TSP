#!/usr/bin/python
# Reminder -- flush regularly

from basic_functions import * 
from tsp_algos import *
from ga import *
from sa import sa

# Begin Main:
N, c, d = read_inp('problems/euc_250')

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

"""
print "Genetic Algo: \n"
t = genetic_algo(d, N)
print_tour(t, N)
print cost_tour(t, d, N)
"""

"""
print "\nRandom Path: \n"
t = range(N)
shuffle(t)
print cost_tour(t, d, N)
"""


print "Simulated Annealing: \n"
sTour = greedy_tour(d, N)
t = sa(sTour, 10, 2.4, 1000, get_random_neighbour(d,1), get_deltaE(d), get_nextTemp(.5))
print_tour(t, N)
print cost_tour(t, d, N)

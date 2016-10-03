#!/usr/bin/python
# Reminder -- flush regularly

from basic_functions import * 
from tsp_algos import *
from ga import *
from sa import sa

# # Begin Main:
# N, c, d = read_inp('problems/euc_250')

N, c, d = read_inp_stdin()

# print "Nearest Neighbour:"
# t = greedy_tour(d, N)
# # print_tour(t, N)
# print cost_tour(t, d, N)


"""
print "\n\nSaving Heuristic: \n"
t = savings_heuristic(d, N)
print_tour(t, N)
print cost_tour(t, d, N)
"""


# print "Genetic Algo:"
t = genetic_algo(d, N)
# if(check_valid_tour(t, N)):
# 	print "Passed tour"
# 	# print_tour(t, N)
# 	print cost_tour(t, d, N)
# 	show_tour(t,c)
# else:
# 	print "Failed tour"
# 	print_tour(t, N)


"""
print "\nRandom Path: \n"
t = range(N)
shuffle(t)
print cost_tour(t, d, N)
"""


# print "Simulated Annealing:"
# # sTour = greedy_tour(d, N)
# n = 100
# tours = []
# # tours.append(sTour)
# for i in range(n):
# 	temp = range(1,N+1)
# 	shuffle(temp)
# 	tours.append(temp)
# saTours = []
# cost = []
# for i in range(len(tours)):
# 	saTours.append(sa(tours[i], 110, 10, 10, get_random_neighbour(d,1), get_deltaE(d), get_nextTemp(.8)))
# 	cost.append(cost_tour(saTours[i], d, N))
# t = min(zip(cost, saTours))[1]
# if(check_valid_tour(t, N)):
# 	print "Passed tour"
# 	# print_tour(t, N)
# 	print cost_tour(t, d, N)
# else:
# 	print "Failed tour"
# 	# print_tour(t, N)
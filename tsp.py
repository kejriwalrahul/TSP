#!/usr/bin/python
# Reminder -- flush regularly

from basic_functions import * 

# Basic greedy algo starting from city 1, and adding closest city to hanging node in partial tour
def greedy_tour(dist, N):
	tour    = [ 1 ]
	visited = { 0 : 1 }
	
	curr = 0
	for i in range(N-1):

		mind = float('inf')
		minc = None
		for j in range(N):
			if j not in visited:
				if dist[i][j] < mind:
					mind = dist[i][j]
					minc = j

		tour.append(minc+1)
		visited[minc] = 1
		curr = minc

	return tour

def savings_heuristic(dist, N):
	tours = []
	# Create initial n-1 tours
	for i in range(N-1):
		tours.append([0, i+1])

	m, n = 0, 0
	# Merge (n-2) tours 
	for i in range(N-2):

		# find best tours to join
		m, n = 0, 0
		maxs = 0
		comb = 0 
		for j in range(N-2):
			if tours[j] == None:
				continue

			for k in range(j+1, N-1):
				if tours[k] == None:
					continue

				curr_sav = dist[0][tours[j][1]]  + dist[0][tours[k][1]]  - dist[tours[j][1]][tours[k][1]]
				if  curr_sav > maxs:
					maxs = curr_sav
					m, n = j, k
					comb = 0

				curr_sav = dist[0][tours[j][1]]  + dist[0][tours[k][-1]] - dist[tours[j][1]][tours[k][-1]]
				if  curr_sav > maxs:
					maxs = curr_sav
					m, n = j, k
					comb = 1

				curr_sav = dist[0][tours[j][-1]] + dist[0][tours[k][1]]  - dist[tours[j][-1]][tours[k][1]]
				if  curr_sav > maxs:
					maxs = curr_sav
					m, n = j, k
					comb = 2

				curr_sav = dist[0][tours[j][-1]] + dist[0][tours[k][-1]] - dist[tours[j][-1]][tours[k][-1]]
				if  curr_sav > maxs:
					maxs = curr_sav
					m, n = j, k
					comb = 3

		if m == n:
			print "\n?\n"
			break

		# merge tours
		if comb == 0:
			tours[m].reverse()
			tours[m] = [0] + tours[m][:-1] + tours[n][1:]
			tours[n] = None
		elif comb == 1:
			tours[m] = tours[n] + tours[m][1:]
			tours[n] = None
		elif comb == 2:
			tours[m] = tours[m] + tours[n][1:]
			tours[n] = None
		else:
			tours[n].reverse()
			tours[m] = tours[m] + tours[n][:-1]
			tours[n] = None		

	return tours[m]

# Begin Main:
N, c, d = read_inp('problems/euc_100')

print "Nearest Neighbour: \n"
t = greedy_tour(d, N)
print_tour(t, N)
print cost_tour(t, d, N)


print "\n\nSaving Heuristic: \n"
t = savings_heuristic(d, N)
print_tour(t, N)
print cost_tour(t, d, N)
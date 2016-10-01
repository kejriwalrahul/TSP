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
		tours.append(({0: i, i: 0}, {i: 0, 0: i}))

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

				curr_sav = dist[tours[j][0][0]][tours[k][0][0]] - dist[0][tours[j][0][0]] - dist[0][tours[k][0][0]]
				if  curr_sav > maxs:
					maxs = curr_sav
					m, n = j, k
					comb = 0

				curr_sav = dist[tours[j][0][0]][tours[k][1][0]] - dist[0][tours[j][0][0]] - dist[0][tours[k][1][0]]
				if  curr_sav > maxs:
					maxs = curr_sav
					m, n = j, k
					comb = 1

				curr_sav = dist[tours[j][1][0]][tours[k][0][0]] - dist[0][tours[j][1][0]] - dist[0][tours[k][0][0]]
				if  curr_sav > maxs:
					maxs = curr_sav
					m, n = j, k
					comb = 2

				curr_sav = dist[tours[j][1][0]][tours[k][1][0]] - dist[0][tours[j][1][0]] - dist[0][tours[k][1][0]]
				if  curr_sav > maxs:
					maxs = curr_sav
					m, n = j, k
					comb = 3

		# merge tours
		if comb == 0:
			x, y = tours[m][0][0], tours[n][0][0]
			# reverse forward and backward pointer maps
			tours[m] = (tours[m][1], tours[m][0])

			tours[m][0][x] 	= y
			tours[m][1][0]	= tours[n][1][0]
			tours[n][0][0]	= tours[m][0][0]
			tours[n][1][y]  = x

			tours[m][0].update(tours[n][0])
			tours[m][1].update(tours[n][1])
			tours[n] = None
		elif comb == 1:
			x, y = tours[m][0][0], tours[n][1][0]
			tours[n][0][y] 	= x
			tours[n][1][0]	= tours[m][1][0]
			tours[m][0][0]  = tours[n][n][0]
			tours[m][1][x]  = y

			tours[n][0].update(tours[m][0])
			tours[n][1].update(tours[m][1])
			tours[m] = tours[n]
			tours[n] = None
		elif comb == 2:
			x, y = tours[m][1][0], tours[n][0][0]
			tours[m][0][x]  = y
			tours[m][1][0]  = tours[n][1][0]
			tours[n][0][0] 	= tours[m][0][0]
			tours[n][1][y]	= x

			tours[m][0].update(tours[n][0])
			tours[m][1].update(tours[n][1])
			tours[n] = None
		else:
			x, y = tours[m][1][0], tours[n][1][0]
			# reverse forward and backward pointer maps
			tours[n] = (tours[n][1], tours[n][0])

			tours[m][0][x] 	= y
			tours[m][1][0]	= tours[n][1][0]
			tours[n][0][0]	= tours[m][0][0]
			tours[n][1][y]  = x

			tours[m][0].update(tours[n][0])
			tours[m][1].update(tours[n][1])
			tours[n] = None		

	return tours[0]

# Begin Main:
N, c, d = read_inp('problems/euc_100')
t = greedy_tour(d, N)

print_tour(t, N)
print cost_tour(t, d, N)

t = savings_heuristic(d, N)
print_tour2(t, N)
print cost_tour2(t, d, N)
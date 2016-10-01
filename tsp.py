#!/usr/bin/python
# Reminder -- flush regularly

def read_inp(file):
	f    = open(file, "r")
	type = f.readline()
	N 	 = int(f.readline())

	coords = []
	for i in range(N):
		coords.append([float(i) for i in f.readline().split(' ')])

	dist = []
	for i in range(N):
		dist.append([float(i) for i in f.readline().split(' ')])

	return N, coords, dist

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

def cost_tour(t, dist, N):
	cost = 0
	for i in range(N-1):
		cost += dist[t[i]-1][t[i+1]-1]
	cost+= dist[t[N-1]-1][t[0]-1]

	return cost

def print_tour(t):
	for i in range(N):
		print t[i],

# Begin Main:
N, c, d = read_inp('problems/euc_100')
t = greedy_tour(d, N)

print_tour(t)
print cost_tour(t, d, N)
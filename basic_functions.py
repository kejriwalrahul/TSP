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

def cost_tour(t, dist, N):
	cost = 0
	for i in range(N-1):
		cost += dist[t[i]-1][t[i+1]-1]
	cost+= dist[t[N-1]-1][t[0]-1]

	return cost

def print_tour(t, N):
	for i in range(N):
		print t[i],

def print_tour2(t, N):
	forw = t[0]
	
	print 1, 
	curr = 0
	for i in range(N-1):
		print forw[curr] + 1
		curr = forw[curr]

def cost_tour2(t, dist, N):
	cost = 0

	forw = t[0]
	curr = 0
	for i in range(N-1):
		cost += dist[curr][forw[curr]]
		curr = forw[curr]
	cost+= dist[curr][0]

	return cost
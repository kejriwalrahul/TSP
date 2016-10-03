from sys import stdin
import matplotlib.pyplot as plt

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

def read_inp_stdin():
	f = stdin
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
	print

def check_valid_tour(t, N):
	seen = [0]*N
	for i in range(N):
		if seen[t[i]-1] == 1:
			print "Seen: ", t[i]
		else:
			seen[t[i]-1] = 1

	flag = 0
	for i in range(N):
		if seen[i] == 0:
			print "Unseen:", i+1
			flag = 1
	
	if flag == 0:
		return True
	else: 
		return False

def check_valid_tour2(t, N):
	seen = [0]*N
	for i in range(N):
		seen[t[i]-1] = 1

	flag = 0
	for i in range(N):
		if seen[i] == 0:
			return False
	return True

def check_pop(pop, N, i):
	for p in pop:
		if not check_valid_tour2(p, N):
			print "Failed ", i
			return False
	return True

def show_tour(t, c):
	x, y = [], []
	for i in t:
		x.append(c[i-1][0])
		y.append(c[i-1][1])

	plt.plot(x, y)
	plt.show()

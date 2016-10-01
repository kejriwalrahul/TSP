from random import randint
from basic_functions import cost_tour
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
				if dist[curr][j] < mind:
					mind = dist[curr][j]
					minc = j

		tour.append(minc+1)
		visited[minc] = 1
		curr = minc

	return tour

# Create n-1 initial tours and merge pair giving best savings n-2 times
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
					maxs, m, n  = curr_sav, j, k
					comb = 0

				curr_sav = dist[0][tours[j][1]]  + dist[0][tours[k][-1]] - dist[tours[j][1]][tours[k][-1]]
				if  curr_sav > maxs:
					maxs, m, n  = curr_sav, j, k
					comb = 1

				curr_sav = dist[0][tours[j][-1]] + dist[0][tours[k][1]]  - dist[tours[j][-1]][tours[k][1]]
				if  curr_sav > maxs:
					maxs, m, n  = curr_sav, j, k
					comb = 2

				curr_sav = dist[0][tours[j][-1]] + dist[0][tours[k][-1]] - dist[tours[j][-1]][tours[k][-1]]
				if  curr_sav > maxs:
					maxs, m, n  = curr_sav, j, k
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

# Use a 2-opt move to generate a random_neighbour
def get_random_neighbour(dist, sel):
	def random_neighbour(cTour):
		l=len(cTour)
		e1=randint(1,l-2)
		e2=randint(e1+1,l-1)
		dup=cTour[e1:e2]
		dup.reverse()
		return cTour[:e1] + dup + cTour[e2:]
	def max2_neighbour(cTour):
		e1, e2 = max2(cTour, dist)
		dup=cTour[e1+1:e2+1]
		dup.reverse()
		return cTour[:e1+1] + dup + cTour[e2+1:]
	if sel==1:
		return random_neighbour
	elif sel==2:
		return max2_neighbour

# Difference in eval
def get_deltaE(dist):
	def deltaE(nTour, cTour):
		ce = cost_tour(cTour, dist, len(cTour))
		ne = cost_tour(nTour, dist, len(nTour))
		return ce - ne
	return deltaE

def get_nextTemp(f):
	def nextTemp(cTemp):
		return cTemp * f
	return nextTemp

def max2(t, d):
	n=len(t)
	e=[]
	for i in range(n-1):
		e.append(d[i][i+1])
	maxd=-1
	maxi=None
	m1=None
	m2=None
	for i in range(n-1):
		if(e[i]>maxd):
			maxd=e[i]
			maxi=i
	m1=i
	maxd=e[i]=-1
	for i in range(n-1):
		if(e[i]>maxd):
			maxd=e[i]
			maxi=i
	m2=i
	return m1, m2

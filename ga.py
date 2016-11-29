from random import shuffle, randint, random
from numpy.random import choice
from basic_functions import cost_tour, print_tour, show_tour
from tsp_algos import greedy_tour
from sa import sa
# for flushing stdout
from sys import stdout

# GA Parameters
n = 200
k = 100
mutate_prob = 0.4
num_iter = 1000

# Using path representation
def initPopulation(dist, N):
	pop = []
	pop.append(greedy_tour(dist, N))
	pop.append(greedy_tour(dist, N))
	pop.append(greedy_tour(dist, N))
	for i in range(n-3):
		temp = range(1, N+1)
		shuffle(temp)
		pop.append(temp)

	return pop

def getFitness(pop, dist, N):
	fitness = []
	for p in pop:
		fitness.append(1.0/cost_tour(p, dist, N))

	return fitness

def selection(population, fitness):
	selected = []
	
	tot = sum(fitness) 
	for i in range(len(fitness)):
		fitness[i] /= tot

	for i in range(n):
		t =  choice(range(n), p=fitness)
		selected.append(population[t][:])

	return selected

def get_alt(m, hashmap):
	while True:
		if m not in hashmap:
			break
		m = hashmap[m]
	return m

# partially mapped crossover
def crossover(p1, p2):
	maxlen = len(p1)
	
	split_1, split_2 = randint(0, maxlen-1), randint(0, maxlen-1)
	# while split_2 == split_1:
	# 	split_2 = randint(0, maxlen-1)
	split_1, split_2 = min(split_1, split_2), max(split_1, split_2)

	# c1, c2 = p1[:], p2[:]
	c1, c2 = [None]*maxlen, [None]*maxlen
	c1[split_1:split_2+1] = p1[split_1:split_2+1] 
	c2[split_1:split_2+1] = p2[split_1:split_2+1] 

	map_1, map_2 = {}, {}
	for i in range(split_1, split_2+1):
		map_1[p1[i]] = p2[i]
		map_2[p2[i]] = p1[i]

	for i in range(split_1) + range(split_2+1, maxlen):
		c1[i] = get_alt(p2[i], map_1)
		c2[i] = get_alt(p1[i], map_2)

	return [c1, c2]

def crossoverPopulation(population):
	offspring = []

	shuffle(population)
	parent_1 = population[:len(population)/2]
	parent_2 = population[len(population)/2:]

	for i in range(len(parent_1)):
		offspring += crossover(parent_1[i], parent_2[i])

	return offspring

# 2 city exchange
def mutateTour(p):
	maxlen = len(p)
	split_1, split_2 = randint(0, maxlen-1), randint(0, maxlen-1)
	while split_2 == split_1:
		split_2 = randint(0, maxlen-1)	
	split_1, split_2 = min(split_1, split_2), max(split_1, split_2)

	mid = p[split_1:split_2+1]
	mid.reverse()
	return p[:split_1] + mid + p[split_2+1:]

def unravel_tour(t, d):
	n = len(t)
	for i in range(n-1):
		for j in range(i+2, n-1):
			if d[t[i]-1][t[i+1]-1] + d[t[j]-1][t[j+1]-1] > d[t[i]-1][t[j]-1] + d[t[i+1]-1][t[j+1]-1]:
				temp = t[i+1:j+1]
				temp.reverse()
				return t[:i+1] + temp + t[j+1:]
	return t

def mutate(population):
	mutation = []
	for p in population: 
		if random() <= mutate_prob:
			mutation.append(mutateTour(p))
		else:
			mutation.append(p)

	return mutation

def optimizePopulation(original_population, derived_population, fitness, dist, N):
	orig_sorted = [x for (y,x) in sorted(zip(fitness, original_population))]
	derv_sorted = sorted(derived_population, key = lambda x: -cost_tour(x, dist, N))

	return derv_sorted[-k:] + orig_sorted[k:]

def best(population, dist, N):
	b = population[0]
	min_cost = cost_tour(population[0], dist, N)
	mini = 0
	
	for i in range(1, n):
		curr_cost = cost_tour(population[i], dist, N)
		if curr_cost < min_cost:
			min_cost, b = curr_cost, population[i]
			mini = i

	return b

def genetic_algo(dist, N):
	population = initPopulation(dist, N)

	# Loop indefinitely, for submission.
	while True:
		# Fixed no of iterations
		for i in range(num_iter):
			fitness 	= getFitness(population, dist, N)
			selected 	= selection(population, fitness)
			offspring	= crossoverPopulation(selected)
			mutated		= mutate(offspring)
			# mutated		= offspring
			optimalPop  = optimizePopulation(population, mutated, fitness, dist, N)
			population = optimalPop

			# unraveled = unravel_tour(population[-1], dist)
			# population[0] = unraveled

			# print the best tour:
			# print_tour(best(population, dist, N), N)
			print cost_tour(best(population, dist, N), dist, N)
			stdout.flush()

	return best(population, dist, N)
	# return population[-1]

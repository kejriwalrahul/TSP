from random import shuffle, randint, random
from numpy.random import choice
from basic_functions import cost_tour

# GA Parameters
n = 20
k = 10
mutate_prob = 0.1

# Using path representation
def initPopulation(dist, N):
	pop = []
	for i in range(n):
		temp = range(N)
		shuffle(temp)
		pop.append(temp)

	return pop

def getFitness(pop, dist, N):
	fitness = []
	for p in pop:
		fitness.append(cost_tour(p, dist, N))

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

# partially mapped crossover
def crossover(p1, p2):
	maxlen = len(p1)
	
	split_1, split_2 = randint(0, maxlen-1), randint(0, maxlen-1)
	while split_2 == split_1:
		split_2 = randint(0, maxlen)

	print split_1, split_2, 

	c1, c2 = p1[:], p2[:]
	split_1, split_2 = min(split_1, split_2), max(split_1, split_2)
	
	print split_1, split_2

	map_1, map_2 = {}, {}
	for i in range(split_1, split_2+1):
		map_1[p1[i]] = p2[i]
		map_2[p2[i]] = p1[i]

	for i in range(split_1) + range(split_2+1, maxlen):
		c1[i] = p2[i] if p2[i] not in map_1 else map_1[p2[i]] 
		c2[i] = p1[i] if p1[i] not in map_2 else map_2[p1[i]] 

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
	split_1, split_2 = randint(0, maxlen), randint(0, maxlen)
	while split_2 == split_1:
		split_2 = randint(0, maxlen)	

	mid = p[split_1:split_2+1]
	mid.reverse()
	return p[:split_1] + mid + p[split_2+1:]

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
	derv_sorted = sorted(derived_population, key = lambda x: cost_tour(x, dist, N))

	return orig_sorted[k:] + derv_sorted[-k:]

def best(population):
	b = population[0]
	min_cost = cost_tour(population[0])
	
	for i in range(1, n):
		curr_cost = cost_tour(population[i])
		if curr_cost < min_cost:
			min_cost, b = curr_cost, population[i]

	return b

def genetic_algo(dist, N):
	population = initPopulation(dist, N)

	# Fixed no of iterations
	for i in range(100):
		fitness 	= getFitness(population, dist, N)
		selected 	= selection(population, fitness)
		offspring	= crossoverPopulation(selected)
		mutated		= mutate(offspring)
		optimalPop  = optimizePopulation(population, mutated, fitness, dist, N)

		population = optimalPop

	return best(population)

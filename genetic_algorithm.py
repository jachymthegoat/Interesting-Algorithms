
import random

capacity = 40
items = [(1,10,5),(2,8,11),(3,4,7),(4,18,14),(5,5,3),(6,17,10)]
population_size = 20
generations = 100
mutation_rate = 1/6

def create_one():
    one = []
    for i in range(len(items)):
        one.append(random.randint(0, 1))
    return one

def create_population():
    population = []
    for i in range(population_size):
        population.append(create_one())
    return population

def fitness(one):
    total_value = 0
    total_weight = 0
    for i in range(len(items)):
        if one[i] == 1:
            total_weight += items[i][1]
            total_value += items[i][2]
    if total_weight > capacity:
        return 0
    return total_value

def select_parents(population):
    sorted_list = sorted(population, key=fitness, reverse=True)
    return sorted_list[0], sorted_list[1]

def crossover(parent1, parent2):
    child1 = parent1[:len(parent1)//2] + parent2[len(parent2)//2:]
    child2 = parent2[:len(parent2)//2] + parent1[len(parent1)//2:]
    return child1, child2

def mutation(one):
    new_one = one[:]
    for i in range(len(new_one)):
        if random.random() < mutation_rate:
            new_one[i] = 1 - new_one[i]
    return new_one

def new_population(population):
    new_population = []
    p1, p2 = select_parents(population)
    for i in range(population_size // 2):
        child1, child2 = crossover(p1, p2)
        new_population.append(mutation(child1))
        new_population.append(mutation(child2))
    return new_population

population = create_population()

for generation in range(generations):
    population = new_population(population)
    best_one = max(population, key=fitness)
    print(f"Generace = {generation}: Best = {best_one}, vysledek = {fitness(best_one)}")
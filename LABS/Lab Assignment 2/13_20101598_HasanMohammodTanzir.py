

import random as rnd

khuchra = []
player_dictionary = {}
with open('input1.txt', 'r') as rf:
    length, goal = rf.readline().split()
    for i in rf.readlines():
        khuchra.append(i.split())
    for j in khuchra:
        player_dictionary[str(j[0])] = int(j[1])
max_iter = 1000

def populating():
    population = []
    for i in range(500):
        temp = []
        for j in range(int(length)):
            temp.append(rnd.randint(0,1))
        population.append(temp)
    return population


population = populating()


def total_runs (parent):
    total_runs = 0
    count = 0
    for key, val in player_dictionary.items():
        if parent[count] == 1:
            total_runs += val
            count += 1
        else:
            count += 1
    return total_runs


def fitness_check(parent):
    value = total_runs(parent) - int(goal)
    return value


def random_selection(population):
    parent = rnd.choice(population)
    return parent


def crossover(n,parent):
    for i in range(n):
        rnd.shuffle(parent)
    return parent


def mutation(child):
    random_index = rnd.randint(0,len(child)-1)
    rand_value = rnd.randint(0, 1)
    child[random_index] = rand_value
    return child
def BCB():
    team = []
    for key, val in player_dictionary.items():
        team.append(key)
    return team
boolean = None
result_sequence = []
while max_iter > 0:
    new_population = []
    for i in range(len(population)):

        parent = random_selection(population)
        child = crossover(6, parent)
        if rnd.uniform(0,1) < 1.0:
            child = mutation(child)
        if total_runs(child) == int(goal):
            result_sequence = child
            boolean = True
            break
        new_population.append(child)
    if boolean == True:
        break
    population = new_population
    max_iter -= 1
if boolean == True:
    print(BCB())
    for i in result_sequence:
        print(i, end="")
else:
    print(BCB())
    print(-1)
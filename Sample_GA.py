from fuzzywuzzy import fuzz
import random
import string

# ------puplic variables can put in other file ------

# string we need to match
in_str = None

# length of this string
in_str_len = None

# no. of population in one generation
population = 20

# no. of max. genaration
generations = 1000
# ----------------------------------------------------


# main class that present our elements
class Agent:

    # constructor
    def __init__(self, length):

        # string.letters => return all letters
        # random.choice(input) => make arondomly choice from input
        # for _ in xrange(input) => repeat operation fot inout times
        self.string = ''.join(random.choice(string.ascii_letters)
                              for _ in range(length))
        self.fitness = -1

    # it is almost like .tostring in .net
    # it is how our class will be in printing
    def __str__(self):

        return 'String: {0}  Fitness: {1}'.format(self.string, self.fitness)

# main function of GA


def GA():

    # Generate initail pop elements
    agents = init_agents(population, in_str_len)

    for generation in range(generations):

        print('Generation: {}'.format(generation))

        agents = fitness(agents)

        agents = selection(agents)

        agents = crossover(agents)

        agents = mutation(agents)

        if any(agent.fitness >= 95 for agent in agents):

            print('Done!! ')
            exit(0)


# Create elements of the first generation
def init_agents(population, length):

    return [Agent(length) for _ in range(population)]


# Create Fitness function
def fitness(agents):

    for agent in agents:

        agent.fitness = fuzz.ratio(agent.string, in_str)

    return agents


# Select the top fittest elements
def selection(agents):

    agents = sorted(agents, key=lambda agent: agent.fitness, reverse=True)

    print('\n'.join(map(str, agents)))

    agents = agents[:int(0.2 * len(agents))]

    return agents


# Crossover
def crossover(agents):

    offspring = []

    for _ in range(int((population - len(agents)) / 2) + 1):

        parent1 = random.choice(agents)
        parent2 = random.choice(agents)

        child1 = Agent(in_str_len)
        child2 = Agent(in_str_len)

        split = random.randint(0, in_str_len)

        child1.string = parent1.string[0:split] + \
            parent2.string[split:in_str_len]
        child2.string = parent2.string[0:split] + \
            parent1.string[split:in_str_len]

        offspring.append(child1)
        offspring.append(child2)

    agents.extend(offspring)

    return agents


# Mutation
def mutation(agents):

    for agent in agents:

        for index, val in enumerate(agent.string):

            if random.uniform(0.0, 1.0) <= 0.2:

                agent.string = agent.string[0:index] + random.choice(
                    string.ascii_letters) + agent.string[index+1:in_str_len]

    return agents


# To fire
if __name__ == '__main__':

    in_str = 'aya'

    in_str_len = len(in_str)

    GA()

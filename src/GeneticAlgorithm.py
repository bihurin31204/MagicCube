import numpy as np
import random
from State import State

GENES = 125

class GeneticAlgorithm():
    def __init__(self, population_size, max_iteration, mutation_rate):
        self.population_size = population_size
        self.max_iteration = max_iteration
        self.mutation_rate = mutation_rate
        self.population = np.array([np.random.choice(np.arange(1, 126), size=125, replace=False) for _ in range(self.population_size)])
    
    def random_selection(self):
        fitnesses = np.array([self.fitness(individual) for individual in self.population])
        probabilities = fitnesses / fitnesses.sum()
        parent_index = np.random.choice(np.arange(self.population_size), p=probabilities)
        parent = self.population[parent_index]
        return parent
        
    # Crossover function (single-point crossover)
    def reproduce(self, parent1, parent2):
        point = random.randint(1, GENES-1)
        child = np.concatenate((parent1[:point], parent2[point:]))
        return child
    
    def mutate(self, individual):
        point = random.randrange(GENES)
        gene = random.randint(1, GENES)
        individual[point] = gene
        return individual
    
    def get_feature_sum(self, individual):
        state = np.copy(individual).reshape(5, 5, 5)

        # pillars (25)
        pillar_sum = np.sum(state, axis=0).flatten()

        # rows (25)
        row_sum = np.sum(state, axis=2).flatten()

        # collumns (25)
        column_sum = np.sum(state, axis=1).flatten()

        # space diagonals (4)
        space_diagonals = []
        space_diagonals.append([state[i, i, i] for i in range(5)])
        space_diagonals.append([state[i, i, 4 - i] for i in range(5)])
        space_diagonals.append([state[i, 4 - i, i] for i in range(5)])
        space_diagonals.append([state[4 - i, i, i] for i in range(5)])
        space_diagonal_sum = np.sum(space_diagonals, axis=1)

        # diagonals (30)
        diagonals = []
        for n in range(5):
            # plane xy
            diagonals.append([state[i, i, n] for i in range(5)])
            diagonals.append([state[i, 4-i, n] for i in range(5)])
            # plane xz
            diagonals.append([state[i, n, i] for i in range(5)])
            diagonals.append([state[i, n, 4-i] for i in range(5)])
            # plane yz
            diagonals.append([state[n, i, i] for i in range(5)])
            diagonals.append([state[n, i, 4-i] for i in range(5)])
        diagonal_sum = np.sum(diagonals, axis=1)

        # collect all features
        feature_sum = np.concatenate((pillar_sum, row_sum, column_sum, space_diagonal_sum, diagonal_sum))

        return feature_sum
    
    def fitness(self, individual):
        feature_sum = self.get_feature_sum(individual)

        # calculate fitness
        value = 0
        for x in feature_sum:
            value -= abs(x-315)

        return 10000 + value
    
    def evaluate(self, individual):
        feature_sum = self.get_feature_sum(individual)
        
        # calculate state value
        value = 0
        for x in feature_sum:
            value -= abs(x-315)

        return value
    
    def is_goal_state_in_population(self):
        values = np.array([self.evaluate(individual) for individual in self.population])
        return np.any(values == 0)
    
    def get_best_individual(self):
        values = np.array([self.evaluate(individual) for individual in self.population])
        best_index = np.argmax(values)
        best_individual = self.population[best_index]
        return best_individual
    
    def search(self):
        iteration = 1
        values = [self.evaluate(self.get_best_individual())]
        while not self.is_goal_state_in_population() and iteration <= self.max_iteration:
            print(f'iteration: {iteration}')
            offspring = []
            for _ in range(self.population_size):
                # Selection
                parent1 = self.random_selection()
                parent2 = self.random_selection()

                # Crossover / Reproduce
                child = self.reproduce(parent1, parent2) # Crossover antara dua parent

                # Mutation
                random_probability = random.random()
                if random_probability > self.mutation_rate:
                    child = self.mutate(child)
                
                offspring.append(child)
            self.population = offspring
            best_individual = self.get_best_individual()
            best_individual_value = self.evaluate(best_individual)
            print(f'best individual value: {best_individual_value}')
            values.append(best_individual_value)
            iteration += 1
        final_state = State(best_individual)
        return final_state, values
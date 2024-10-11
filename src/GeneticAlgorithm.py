class GeneticAlgorithm(Algorithm):
    def __init__(self, population_size, mutation_rate, crossover_rate):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.population = self.initialize_population()

    def initialize_population():
        return np.array([1, 2, 3, ..., 125])

    def search (self):
        while not self.is_goal_state_in_population () :
            parents = self.select_parents ()
            offspring = []
            for i in range(0, len(parents), 2):
                parent1, parent2 = parents [i, parents [i + 1]
                if (random_probability) < self.crossover_rate:
                    child1, child2 = self.crossover (parent1, parent2) # Crossover antara dua parent
                else:
                    child1, child2 = parent1, parent2
                offspring.append(child1)
                offspring.append(child2)
            for child in offspring:
                if random_probability() < self.mutation_rate:
                    self.mutate(child) # Mutasi pada child

            self.population = self.select_survivors (offspring) # Seleksi generasi berikutnya
        return self.get_best_individual()


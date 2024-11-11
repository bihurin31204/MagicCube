from State import State
import random
import numpy as np

class SimulatedAnnealing():
    def __init__(self, initial_temperature, cooling_rate):
        self.current_state = State()
        self.temperature = initial_temperature
        self.cooling_rate = cooling_rate

    def generate_successors(self):
        indices = [(i, j, k) for i in range(5) for j in range(5) for k in range(5)]
        successors = []
        for i in range(len(indices)):
            for j in range(i + 1, len(indices)):  # Pastikan tidak menukar elemen yang sama
                index_1 = indices[i]
                index_2 = indices[j]
                successor = State()
                successor.state = np.copy(self.current_state.state)
                successor.state[index_1], successor.state[index_2] = self.current_state.state[index_2], self.current_state.state[index_1]
                successor.value = successor.evaluate()
                successors.append(successor)
        successors = np.array(successors)
        return successors
    
    def select_random_successor(self, successors):
        random_index = random.randrange(len(successors))
        neighbor = successors[random_index]
        return neighbor

    def search(self):
        print(self.current_state)
        print(f'initial state value: {self.current_state.value}')
        local_optima = 0
        probs = []
        values = [self.current_state.value]
        while not self.current_state.is_goal_state() and self.temperature > 0:
            successors = self.generate_successors()
            neighbor = self.select_random_successor(successors) # Pilih tetangga acak
            delta =  neighbor.value - self.current_state.value
            if delta > 0:
                self.current_state = neighbor # Pindah jika lebih baik
                print(f'current state value: {neighbor.value}')
            else:
                random_probability = random.uniform(0,1)
                if random_probability < np.exp(delta / self.temperature):
                    self.current_state = neighbor # Pindah dengan probabilitas
                    print(f'current state value: {neighbor.value}')
                    local_optima += 1
            probs.append(np.exp(delta / self.temperature))
            self.temperature -= self.cooling_rate # Kurangi temperatur
            print(f'current temperature: {round(self.temperature, 1)}')
            values.append(self.current_state.value)
        print('terminate')
        print(f'final state value: {self.current_state.value}')
        print(f'local optima freq: {local_optima}')
        return self.current_state, values, probs
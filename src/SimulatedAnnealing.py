import State
import random
import math
import numpy as np

class SimulatedAnnealing():
    def _init_(self, initial_temperature, cooling_rate):
        self.temperature = initial_temperature
        self.cooling_rate = cooling_rate
        # TODO
        # masukin elemen state dan nilai goal_value
        self.current_state = State(np.array([]), 0)

    def generate_neighbors(self):
        # TODO
        # cari cara untuk generate neighbors
        return []
    
    def select_random_neighbor(self, neighbors):
        return random.choice(neighbors)

    def search(self):
        while not self.current_state.is_goal_state() and self. temperature > 0:
            neighbors = self.generate_neighbors()
            random_neighbor = self.select_random_neighbor(neighbors) # Pilih tetangga acak
            delta = random_neighbor.evaluate_state() - self.current_state.evaluate_state()
            if delta > O:
                self.current_state = random_neighbor # Pindah jika lebih baik
        else:
            random_probability = random.uniform(0, 1)
            if random_probability < math.exp(delta / self.temperature):
                self.current_state = random_neighbor # Pindah dengan probabilitas
            self.temperature -= self.cooling_rate # Kurangi temperatur
        return self.current_state

sa = SimulatedAnnealing(200, 1)
print(type(sa))
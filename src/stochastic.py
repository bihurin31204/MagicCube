import numpy as np
import random
import time
import matplotlib.pyplot as plt
import State

class StochasticHillClimbing:
    def __init__(self, max_iterations=100000, tolerance=1):
        self.max_iterations = max_iterations
        self.tolerance = tolerance
        self.value_history = []

    def generate_initial_state(self):
        numbers = list(range(1, 126))  # Angka dari 1 hingga 125
        cube = np.zeros((5, 5, 5), dtype=int)
        random.shuffle(numbers)
        idx = 0
        for i in range(5):
            for j in range(5):
                for k in range(5):
                    cube[i][j][k] = numbers[idx]
                    idx += 1
        return State.State(cube)  # Bungkus dalam objek State

    def swap_two_numbers(self, state):
        cube = state.state
        i1, j1, k1 = random.randint(0, 4), random.randint(0, 4), random.randint(0, 4)
        i2, j2, k2 = random.randint(0, 4), random.randint(0, 4), random.randint(0, 4)

        # Pastikan posisi berbeda
        while i1 == i2 and j1 == j2 and k1 == k2:
            i2, j2, k2 = random.randint(0, 4), random.randint(0, 4), random.randint(0, 4)

        # Tukar dua angka
        cube[i1, j1, k1], cube[i2, j2, k2] = cube[i2, j2, k2], cube[i1, j1, k1]
        return State.State(cube)  # Kembalikan state baru

    def search(self):
        current_state = self.generate_initial_state()
        current_value = current_state.evaluate()
        self.value_history.append(current_value)
        
        iterations = 0

        print("Initial Objective Value:", current_value)

        while iterations < self.max_iterations:
            new_state = self.swap_two_numbers(current_state)
            new_value = new_state.evaluate()

            # Periksa apakah state baru adalah perbaikan
            if new_value > current_value:
                current_state = new_state
                current_value = new_value
                print(f"Iteration {iterations + 1}: Improved Objective Value = {current_value}")

            self.value_history.append(current_value)
            iterations += 1

            #print(f"State at Iteration {iterations}: {current_state.state}")
        
            if current_state.is_goal_state():
                break

        self.plot_results(self.value_history)
        return current_value

    def plot_results(self, value_history):
        plt.figure(figsize=(10, 6))
        plt.plot(value_history, marker='o', linestyle='-', color='b', markersize=4)
        plt.xlabel('Iterations')
        plt.ylabel('Objective Function Value')
        plt.title('Objective Function Value over Iterations')
        plt.grid(True)
        plt.show()
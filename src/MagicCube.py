import time
import matplotlib.pyplot as plt
from SteepestAscentHC import SteepestAscentHC as SAHC
from HCWithSidewaysMove import HCWithSidewaysMove as HCSM
from StochasticHC import StochasticHC as SHC
from RandomRestartHC import RandomRestartHC as RRHC
from SimulatedAnnealing import SimulatedAnnealing as SA
from GeneticAlgorithm import GeneticAlgorithm as GA

# Hill Climbing With Sideways Move
MAX_SIDEWAYS_MOVE = 10

# Stochastic Hill Climbing
SHC_MAX_ITERATION = 100

# Random Restart Hill Climbing
MAX_RESTART = 2

# Simulated Annealing
INITIAL_TEMPERATURE = 100.0
COOLING_RATE = 1.0

# Genetic Algorithm
POPULATION_SIZE = 100
GA_MAX_ITERATION = 100
MUTATION_RATE = 0.5

class MagicCube():
    def __init__(self, alg):
        if alg == 'sahc':
            self.alg = alg
            self.algorithm = SAHC()
        elif alg == 'hcsm':
            self.alg = alg
            self.algorithm = HCSM(MAX_SIDEWAYS_MOVE)
        elif alg == 'shc':
            self.alg = alg
            self.algorithm = SHC(SHC_MAX_ITERATION)
        elif alg == 'rrhc':
            self.alg = alg
            self.algorithm = RRHC(MAX_RESTART)
        elif alg == 'sa':
            self.alg = alg
            self.algorithm = SA(INITIAL_TEMPERATURE, COOLING_RATE)
        elif alg == 'ga':
            self.alg = alg
            self.algorithm = GA(POPULATION_SIZE, GA_MAX_ITERATION, MUTATION_RATE)
        else:
            print('Invalid algorithm!')
    
    def solve(self):
        assert self.algorithm is not None, "No algorithm selected!"
        start_time = time.time()
        result = self.algorithm.search()
        end_time = time.time()
        self.final_state = result[0]
        values = result[1]
        print(self.final_state)
        print(self.final_state.value)
        print(f'duration: {end_time-start_time} seconds')

        # Plot
        if self.alg == 'rrhc':
            plt.title("State Value Plot")
            plt.xlabel("Iteration")
            plt.ylabel("Value")
            for key, value in values.items():
                plt.plot(value, label=str(key))
            plt.legend()
            plt.show()
        else:
            if self.alg == 'sa':
                probs = result[2]
                plt.title("Probabilities Plot")
                plt.xlabel("Iteration")
                plt.ylabel("Probabilities")
                plt.plot(probs)
                plt.show()
            plt.title("State Value Plot")
            plt.xlabel("Iteration")
            plt.ylabel("Value")
            plt.plot(values)
            plt.show()
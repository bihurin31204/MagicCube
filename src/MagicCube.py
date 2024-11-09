#import SteepestAscentHC as HC
#import SimulatedAnnealing as SA
#import GeneticAlgorithm as GA
import stochastic as ST
import State

class MagicCube():
    def __init__(self, algorithm):
        if algorithm == 'st':
            self.algorithm = ST.StochasticHillClimbing()
        else:
            raise ValueError("Unknown algorithm type")
    
    def solve(self):
        self.final_value = self.algorithm.search()
        #print("Final State:\n", self.final_state.state)
        print("Final Objective Value:", self.final_value)

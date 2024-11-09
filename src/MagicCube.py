#import SteepestAscentHC as HC
#import SimulatedAnnealing as SA
#import GeneticAlgorithm as GA
import stochastic as ST

class MagicCube():
    def __init__(self, algorithm):
        #if algorithm == 'hc':
            #self.algorithm = HC()
        #if algorithm == 'sa':
            #self.algorithm = SA()
        #elif algorithm == 'ga':
            #self.algorithm = GA()
        if algorithm == 'st':
            self.algorithm = ST.StochasticHillClimbing()
        else:
            raise ValueError("Unknown algorithm type")
    
    def solve(self):
        # print state setiap langkah sampe mentok
        self.final_state = self.algorithm.search()
        print("Final State:\n", self.final_state.state)
        print("Final Objective Value:", self.final_state.evaluate())
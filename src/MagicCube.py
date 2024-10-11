import SteepestAscentHC as HC
import SimulatedAnnealing as SA
import GeneticAlgorithm as GA

class MagicCube():
    def __init__(self, algorithm):
        if algorithm == 'hc':
            self.algorithm = HC()
        elif algorithm == 'sa':
            self.algorithm = SA()
        elif algorithm == 'ga':
            self.algorithm = GA()
        else:
            pass
    
    def solve(self):
        # print state setiap langkah sampe mentok
        self.final_state = self.algorithm.search()
        print(self.final_state)
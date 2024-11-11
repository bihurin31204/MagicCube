from State import State
import numpy as np

class HillClimbing():
    def __init__(self):
        self.current_state = State()
    
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
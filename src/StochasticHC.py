import random
from HillClimbing import HillClimbing

class StochasticHC(HillClimbing):
    def __init__(self, max_iteration):
        super().__init__()
        self.max_iteration = max_iteration

    def select_random_successor(self, successors):
        random_index = random.randrange(len(successors))
        random_successor = successors[random_index]
        return random_successor
    
    def search(self):
        print(self.current_state)
        print(f'initial state value: {self.current_state.value}')
        values = [self.current_state.value]
        for _ in range(self.max_iteration):
            successors = self.generate_successors() # Hasilkan tetangga dari current state
            neighbor = self.select_random_successor(successors) # Pilih tetangga terbaik
            if neighbor.value > self.current_state.value:
                self.current_state = neighbor # Update current state
            print(f'current state value: {self.current_state.value}')
            values.append(self.current_state.value)

        print('terminate')
        print(f'final state value: {self.current_state.value}')
        return self.current_state, values
from HillClimbing import HillClimbing

class SteepestAscentHC(HillClimbing):
    def __init__(self):
        super().__init__()
    
    def select_highest_value_successor(self, successors):
        best_successor_index = 0
        best_value = successors[0].value
        for i in range(1, len(successors)):
            next_value = successors[i].value
            if (next_value > best_value):
                best_successor_index = i
                best_value = next_value
        neighbor = successors[best_successor_index]
        return neighbor

    def search(self):
        print(self.current_state)
        print(f'initial state value: {self.current_state.value}')
        values = [self.current_state.value]
        iteration_count = 0
        while not self.current_state.is_goal_state():
            successors = self.generate_successors() # Hasilkan tetangga dari current state
            neighbor = self.select_highest_value_successor(successors) # Pilih tetangga terbaik
            iteration_count += 1
            if neighbor.value > self.current_state.value:
                self.current_state = neighbor # Update current state
                print(f'current state value: {self.current_state.value}')
                values.append(self.current_state.value)
            else:
                break
        print('terminate')
        print(f'final state value: {self.current_state.value}')
        print(f'iteration count: {iteration_count}')
        return self.current_state, values
from State import State
from HillClimbing import HillClimbing

class RandomRestartHC(HillClimbing):
    def __init__(self, max_restart):
        self.max_restart = max_restart
    
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
        values_per_restart = {}
        for restart in range(1, self.max_restart+1):
            self.current_state = State()
            print(self.current_state)
            print(f'initial state value: {self.current_state.value}')
            values = [self.current_state.value]
            while not self.current_state.is_goal_state():
                successors = self.generate_successors() # Hasilkan tetangga dari current state
                neighbor = self.select_highest_value_successor(successors) # Pilih tetangga terbaik
                if neighbor.value > self.current_state.value:
                    self.current_state = neighbor # Update current state
                    print(f'current state value: {self.current_state.value}')
                    values.append(self.current_state.value)
                else:
                    print(f'restart remaining: {self.max_restart-restart}')
                    break
            values_per_restart[restart] = values
            print(f'final state value: {self.current_state.value}')
            if self.current_state.is_goal_state():
                break
        print('terminate')
        return self.current_state, values_per_restart
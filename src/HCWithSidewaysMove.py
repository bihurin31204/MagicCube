from HillClimbing import HillClimbing

class HCWithSidewaysMove(HillClimbing):
    def __init__(self, max_sideways_move):
        super().__init__()
        self.max_sideways_move = max_sideways_move
    
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
        sideways_move = 0
        while not self.current_state.is_goal_state() and sideways_move < self.max_sideways_move:
            successors = self.generate_successors() # Hasilkan tetangga dari current state
            neighbor = self.select_highest_value_successor(successors) # Pilih tetangga terbaik
            iteration_count += 1
            if neighbor.value > self.current_state.value:
                self.current_state = neighbor # Update current state
                print(f'current state value: {self.current_state.value}')
                values.append(self.current_state.value)
            elif neighbor.value == self.current_state.value and sideways_move < self.max_sideways_move:
                self.current_state = neighbor # Update current state
                print(f'current state value: {self.current_state.value}')
                values.append(self.current_state.value)
                sideways_move += 1
                print(f'sideways move remaining: {self.max_sideways_move-sideways_move}')
            else:
                break  # Jika tidak ada perbaikan, hentikan
        print('terminate')
        print(f'final state value: {self.current_state.value}')
        print(f'iteration count: {iteration_count}')
        return self.current_state, values
import State

class SteepestAscentHC():
    def __init__(self):
        pass
    self.current_state = State(np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], ..., []]), 0)

    def search(self):
        while not self.current_state.is_goal_state():
            neighbors = self.generate_neighbors() # Hasilkan tetangga dari current current state
            best_neighbor = self.select_best_neighbor(neighbors) # Pilih tetangga terbaik
            if self.evaluate_state(best_neighbor) > self.evaluate_state(self.current_state):
                self.current_state = best_neighbor # Update current state
            else:
                break  # Jika tidak ada perbaikan, hentikan
        return self.current_state


class State():
    def __init__(self, state, goal_value):
        self.state = state
        self.goal_value = goal_value

    def evaluate(self):
        # TODO
        # Hitung maksimal jumlah baris/kolom/diagonal yang memiliki sum yang sama
        return max()

    def is_goal_state(self):
        return self.evaluate() == self.goal_value
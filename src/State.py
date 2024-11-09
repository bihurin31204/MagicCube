import numpy as np

class State():
    def __init__(self, state=None):
        if state is not None:
            self.state = state.reshape(5, 5, 5)
        else:
            self.state = self.generate_state()
        self.value = self.evaluate()

    def generate_state(self):
        state = np.random.choice(np.arange(1, 126), size=125, replace=False).reshape((5, 5, 5))
        return state

    def evaluate(self):
        # pillars (25)
        pillar_sum = np.sum(self.state, axis=0).flatten()

        # rows (25)
        row_sum = np.sum(self.state, axis=2).flatten()

        # collumns (25)
        column_sum = np.sum(self.state, axis=1).flatten()

        # space diagonals (4)
        space_diagonals = []
        space_diagonals.append([self.state[i, i, i] for i in range(5)])
        space_diagonals.append([self.state[i, i, 4 - i] for i in range(5)])
        space_diagonals.append([self.state[i, 4 - i, i] for i in range(5)])
        space_diagonals.append([self.state[4 - i, i, i] for i in range(5)])
        space_diagonal_sum = np.sum(space_diagonals, axis=1)

        # diagonals (30)
        diagonals = []
        for n in range(5):
            # plane xy
            diagonals.append([self.state[i, i, n] for i in range(5)])
            diagonals.append([self.state[i, 4-i, n] for i in range(5)])
            # plane xz
            diagonals.append([self.state[i, n, i] for i in range(5)])
            diagonals.append([self.state[i, n, 4-i] for i in range(5)])
            # plane yz
            diagonals.append([self.state[n, i, i] for i in range(5)])
            diagonals.append([self.state[n, i, 4-i] for i in range(5)])
        diagonal_sum = np.sum(diagonals, axis=1)

        # collect all features
        feature_sum = np.concatenate((pillar_sum, row_sum, column_sum, space_diagonal_sum, diagonal_sum))

        # calculate state value
        self.value = 0
        for x in feature_sum:
            self.value -= abs(x-315)

        return self.value

    def is_goal_state(self):
        return self.value == 0
    
    def __str__(self):
        return np.array2string(self.state, separator=' ')
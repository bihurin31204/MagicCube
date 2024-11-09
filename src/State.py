class State():
    def __init__(self, state, goal_value=109):
        self.state = state
        self.goal_value = goal_value

    def evaluate(self):
        count = 0
        target_sum = 315
        # Hitung maksimal jumlah baris/kolom/diagonal yang memiliki sum yang sama
        #return max()
        #checking baris
        for layer in self.state:
            for row in layer:
                if sum(row) == target_sum:
                    count += 1
               
        #checking kolom     
        for i in range(5):
            for layer in self.state:
                if sum(layer[j][i] for j in range(5)) == target_sum:
                    count += 1
        
        #checking tiang 
        for i in range(5):
            for j in range(5):
                if sum(self.state[k][i][j] for k in range(5)) == target_sum:
                    count += 1
        
        #checking diagonal layer
        for layer in self.state:
            if sum(layer[i][i] for i in range(5)) == target_sum:
                count += 1
            if sum(layer[i][4-i] for i in range(5)) == target_sum:
                count += 1
        
        #checking diagonal ruang
        if sum(self.state[i][i][i] for i in range(5)) == target_sum:
            count += 1
        if sum(self.state[i][i][4-i] for i in range(5)) == target_sum:
            count += 1
        if sum(self.state[i][4-i][i] for i in range(5)) == target_sum:
            count += 1
        if sum(self.state[4-i][i][i] for i in range(5)) == target_sum:
            count += 1
        
        return count

    def is_goal_state(self):
        return self.evaluate() == self.goal_value

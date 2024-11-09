import numpy as np
import random
import time
import matplotlib.pyplot as plt

# Ini belum nge-generate visualisasi kubusnya dalam bentuk array
#Tapi ini hasil obj. fuctionnya paling baik
#Ini fungsi swap-nya dibikin sendiri
# Fungsi untuk menghitung jumlah baris, kolom, tiang, dan diagonal yang memiliki jumlah 315
def objective_function(cube):
    count = 0
    target_sum = 315
    # Mengecek baris (25 baris)
    for layer in cube:
        for row in layer:
            if sum(row) == target_sum:
                count += 1
    
    # Mengecek kolom (25 kolom)
    for i in range(5):
        for layer in cube:
            if sum(layer[j][i] for j in range(5)) == target_sum:
                count += 1
    
    # Mengecek tiang (25 tiang)
    for i in range(5):
        for j in range(5):
            if sum(cube[k][i][j] for k in range(5)) == target_sum:
                count += 1

    # Mengecek diagonal lapisan (30 diagonal)
    for layer in cube:
        if sum(layer[i][i] for i in range(5)) == target_sum:
            count += 1
        if sum(layer[i][4-i] for i in range(5)) == target_sum:
            count += 1
    
    # Mengecek diagonal ruang (4 diagonal)
    if sum(cube[i][i][i] for i in range(5)) == target_sum:
        count += 1
    if sum(cube[i][i][4-i] for i in range(5)) == target_sum:
        count += 1
    if sum(cube[i][4-i][i] for i in range(5)) == target_sum:
        count += 1
    if sum(cube[4-i][i][i] for i in range(5)) == target_sum:
        count += 1

    return count

# Fungsi untuk menghasilkan inisialisasi acak kubus
def generate_initial_state():
    numbers = list(range(1, 126))  # Angka dari 1 hingga 53
    cube = np.zeros((5, 5, 5), dtype=int)
    #ini kalau random, pasti beda atau ga ya?
    random.shuffle(numbers)
    idx = 0
    for i in range(5):
        for j in range(5):
            for k in range(5):
                cube[i][j][k] = numbers[idx]
                idx += 1
    return cube

# Fungsi untuk menukar dua angka acak dalam kubus
def swap_two_numbers(cube):
    i1, j1, k1 = random.randint(0, 4), random.randint(0, 4), random.randint(0, 4)
    i2, j2, k2 = random.randint(0, 4), random.randint(0, 4), random.randint(0, 4)
    
    # Pastikan posisi berbeda
    while i1 == i2 and j1 == j2 and k1 == k2:
        i2, j2, k2 = random.randint(0, 4), random.randint(0, 4), random.randint(0, 4)
    
    # Menukar posisi dua angka
    cube[i1, j1, k1], cube[i2, j2, k2] = cube[i2, j2, k2], cube[i1, j1, k1]
    return cube

# Fungsi untuk Stochastic Hill Climbing
def stochastic_hill_climbing(cube, max_iterations=100, tolerance=1):
    start_time = time.time()
    current_state = cube
    current_value = objective_function(current_state)
    value_history = [current_value]
    iterations = 0
    
    print("Initial Cube State:\n", cube)
    #print("Initial Objective Function Value:", current_value)

    while iterations < max_iterations:
        # Buat salinan dari kubus saat ini
        new_state = np.copy(current_state)
        # Lakukan langkah acak: menukar dua angka
        new_state = swap_two_numbers(new_state)
        new_value = objective_function(new_state)
        
        # Jika nilai objective function baru lebih baik, perbarui
        if new_value > current_value:
            current_state = new_state
            current_value = new_value
        
        # Catat nilai objective function
        value_history.append(current_value)
        iterations += 1
        
        # Jika nilai sudah mencapai nilai maksimum atau tidak ada perbaikan signifikan
        if current_value == 109:
            break

    end_time = time.time()
    return current_state, current_value, value_history, iterations, end_time - start_time

# Fungsi untuk memplot hasil
def plot_results(value_history):
    plt.plot(value_history)
    plt.xlabel('Iterations')
    plt.ylabel('Objective Function Value')
    plt.title('Objective Function Value vs Iterations')
    plt.show()

# Inisialisasi dan menjalankan Stochastic Hill Climbing
initial_cube = generate_initial_state()
final_state, final_value, value_history, iterations, duration = stochastic_hill_climbing(initial_cube)

# Menampilkan hasil
print("Initial Objective Function:", objective_function(initial_cube))
print("Final Objective Function:", final_value)
print("Number of Iterations:", iterations)
print("Duration:", duration, "seconds")

# Plot hasil
plot_results(value_history)
from MagicCube import MagicCube

# Memilih algoritma yang akan digunakan, misalnya 'st' untuk Stochastic Hill Climbing
algorithm_choice = 'st'

# Membuat instance dari MagicCube dengan algoritma yang dipilih
magic_cube_solver = MagicCube(algorithm_choice)

# Memulai proses pencarian solusi dan menampilkan hasilnya
magic_cube_solver.solve()

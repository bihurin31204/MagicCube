from MagicCube import MagicCube

print('1. Steepest Ascent Hill Climbing')
print('2. Hill Climbing With Sideways Move')
print('3. Stochastic Hill Climbing')
print('4. Random Restart Hill Climbing')
print('5. Simulated Annealing')
print('6. Genetic Algorithm\n')

opt = int(input('Select algorithm: '))

algorithms = ['sahc', 'hcsm', 'shc', 'rrhc', 'sa', 'ga']

try:
    algorithm = algorithms[opt-1]
    mc = MagicCube(algorithm)
    mc.solve()
except Exception as e:
    print(f"An error occurred: {e}")
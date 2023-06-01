abscissas = [0.0, 1.0, 2.0]
ordinates = [0.0, 0.0, 1.1]
applicates = [0.0, 1.0, 1.5]
r = 2
dots = zip(abscissas, ordinates, applicates)
print(all(map(lambda x: x[0]**2+x[1]**2+x[2]**2 <= r**2, dots)))
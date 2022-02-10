import math
max_iterations = 200
constant = 0.1
def convergence(second, first, number_of_iterations):
    epsilon = 0.00000001
    if number_of_iterations > max_iterations:
        return True
    for i in range(len(second)):
        for j in range(len(second[0])):
            if math.fabs(second[i][j] - first[i][j]) > epsilon:
                return False
    return True

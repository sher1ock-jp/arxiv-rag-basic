import numpy as np
from python_tsp.heuristics import solve_tsp_simulated_annealing

def solve_tsp(embeddings):
    data = np.array(embeddings)
    x1 = data[:, None, :]
    x2 = data[None, :, :]
    distance_matrix = np.linalg.norm(x1 - x2, axis=-1)
    permutation, distance = solve_tsp_simulated_annealing(distance_matrix)
    return permutation
from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import differential_evolution

# Load the data from the uploaded file
with open("night.txt", "r") as file:
    x = [int(line.strip()) for line in file]

def sliding_window_mae(params, x, betta=10, gamma=20, lower_bound_allow=10000):
    # Extract parameters
    a = params[0]
    k = int(round(params[1]))

    # Constraints
    if a <= 0 or a >= 1 or k <= 3:
        return float('inf')  # Penalize invalid parameters

    margin_on_error = 1 + a
    last_k = []
    abs_e = []
    prediction = False
    iter = -1
    FP = 0
    TP = 0

    while iter < len(x) - 1:
        iter += 1
        syn_count0_dec_diff = x[iter]

        if len(last_k) < k:
            last_k.append(syn_count0_dec_diff)

        elif len(last_k) == k and not prediction:
            last_k.pop(0)
            last_k.append(syn_count0_dec_diff)
            deltas = [last_k[i + 1] - last_k[i] for i in range(k - 1)]
            average_delta = sum(deltas) / len(deltas)
            syn_persec_exp = last_k[-1] + average_delta
            prediction = True

        else:
            last_k.pop(0)
            last_k.append(syn_count0_dec_diff)

            # Compute error
            allow_count = max(margin_on_error * syn_persec_exp, lower_bound_allow)
            
            e_ratio = syn_persec_exp / syn_count0_dec_diff if syn_count0_dec_diff != 0 else float('inf')
            if e_ratio < 1-a:
                FP+=1
            else:
                TP+=1

            abs_e.append(abs(syn_persec_exp - syn_count0_dec_diff))

            # Next prediction
            deltas = [last_k[i + 1] - last_k[i] for i in range(k - 1)]
            average_delta = sum(deltas) / len(deltas)
            syn_persec_exp = max(last_k[-1] + average_delta, 0)

    if not abs_e:
        return float('inf')

    # Cost function: MAE + penalty for sensitivity
    mae = sum(abs_e) / len(abs_e) + betta*k - 1/a + gamma*FP
    return mae
    
    # Normalize the MAE to be between 0 and 1
    # raw_mae = sum(abs_e) / len(abs_e)
    # data_range = max(x) - min(x) if max(x) != min(x) else 1  # Prevent division by zero
    # normalized_mae = raw_mae / data_range

    # # Cost function with normalized MAE
    # cost = normalized_mae + betta * k - 1/a + gamma * FP
    # return cost

# # Initial guess
# initial_guess = [0.5, 5]
# # Bounds: a in (0.01, 0.99), k in [4, 50]
# bounds = [(0.01, 0.99), (3, 50)]
# Run optimization
# result = minimize(sliding_window_mae, initial_guess, args=(x,), bounds=bounds)
# optimized_mae = result.fun
# optimal_a, optimal_k = result.x[0], int(round(result.x[1]))
# print(optimized_mae, optimal_a, optimal_k)

# Define bounds for a and k for global optimization
bounds = [(0.01, 0.99), (3, 10)]  # a in (0,1), k in [4,50]

# Use differential evolution to better explore the space (global optimization)
result_de = differential_evolution(
    func=sliding_window_mae,
    bounds=bounds,
    args=(x,),
    strategy='best1bin',
    maxiter=100,
    popsize=15,
    tol=1e-6,
    mutation=(0.5, 1),
    recombination=0.7,
    seed=42
)

optimized_mae_de = result_de.fun
optimal_a_de, optimal_k_de = result_de.x[0], int(round(result_de.x[1]))

print(optimized_mae_de, optimal_a_de, optimal_k_de)

# Grid of a and k values
a_values = np.linspace(0.01, 0.2, 30)
k_values = np.arange(4, 10)
error_surface = np.zeros((len(a_values), len(k_values)))

# Calculate the cost surface
for i, a in enumerate(a_values):
    for j, k in enumerate(k_values):
        error_surface[i, j] = sliding_window_mae([a, k], x)

# Plot the contour
A, K = np.meshgrid(k_values, a_values)
plt.figure(figsize=(12, 6))
cp = plt.contourf(K, A, error_surface, levels=50, cmap='Spectral_r')
plt.colorbar(cp, label='Cost (MAE + 1/a)')
plt.ylabel('k (Window Size)')
plt.xlabel('a (Sensitivity)')
plt.title('Error Surface: MAE - betta*k - 1/alpha + gamma*FP over k and alpha')
plt.tight_layout()
plt.show()

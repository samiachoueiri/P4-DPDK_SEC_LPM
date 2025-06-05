from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import differential_evolution

# Load the data from the uploaded file
with open("00.txt", "r") as file:
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

# Define bounds for a and k for global optimization
bounds = [(0.01, 0.99), (3, 10)]  # a in (0,1), k in [4,50]
result_de = differential_evolution(func=sliding_window_mae,bounds=bounds,args=(x,),strategy='best1bin',maxiter=100,popsize=15,tol=1e-6,mutation=(0.5, 1),recombination=0.7,seed=42)
optimized_mae_de = result_de.fun
optimal_a_de, optimal_k_de = result_de.x[0], int(round(result_de.x[1]))
print(optimized_mae_de, optimal_a_de, optimal_k_de)

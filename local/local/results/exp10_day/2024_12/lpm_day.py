import time
from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import differential_evolution

max_allowed = 0

def get_mae (x, k, a):
    betta = 10
    gamma = 20
    #declarations
    prediction = False
    lower_bound_allow = 10000 #allow at least 10000 pkts per sec
    margin_on_error = 1+a #allow 20% more pkts
    last_k = []
    abs_e = []
    sps = 1
    FP = 0
    TP = 0
    flood = 0
    iter = -1
    train = []
    global max_allowed

    # with open("00_out.txt", "w") as file:

    while iter < len(x) -1:
        iter +=1
        allow_count = 4000000000
        syn_count0_dec_diff = x[iter]

        if(len(last_k)<k):
            last_k.append(syn_count0_dec_diff)
            file.write(f"{iter} {a} {k} {syn_count0_dec_diff} {syn_count0_dec_diff} {margin_on_error*syn_count0_dec_diff} {0} {0}\n")
            # print("fill window:" , last_k)

        elif (len(last_k)==k and prediction == False):
            last_k.pop(0)
            last_k.append(syn_count0_dec_diff)

            deltas = [last_k[i+1] - last_k[i] for i in range(k - 1)]
            average_delta= sum(deltas) / len(deltas)
            syn_persec_exp = last_k[-1] + average_delta
            file.write(f"{iter} {a} {k} {syn_count0_dec_diff} {syn_persec_exp} {margin_on_error*syn_persec_exp} {0} {0}\n")
            prediction = True

            # print("first prediction:",last_k, syn_persec_exp)

        else: 
            # print("predicted:",syn_persec_exp,"VS. actual:",syn_count0_dec_diff)

            # last_k.pop(0)
            # last_k.append(syn_count0_dec_diff)

            allow_count = max(margin_on_error*syn_persec_exp,lower_bound_allow)
            e_ratio = syn_persec_exp / syn_count0_dec_diff if syn_count0_dec_diff != 0 else float('inf')
            
            if e_ratio < 1-a:
                FP+=1
                train.append(syn_count0_dec_diff)
                print("------------------------------------------------fix a:",e_ratio)
            else:
                TP+=1
                train.append(syn_count0_dec_diff)

            if (e_ratio<1-a):
                if (syn_count0_dec_diff > max_allowed):
                    flood = 1
                else:
                    print(f"Observed is: {syn_count0_dec_diff} and max_allowed is {max_allowed}")
                    margin_on_error = 1+a
                    last_k.pop(0)
                    last_k.append(syn_count0_dec_diff)
                    # print(last_k)
                    # syn_count0_dec_prev = syn_count0_dec

                    deltas = [last_k[i+1] - last_k[i] for i in range(k - 1)]
                    average_delta= sum(deltas) / len(deltas)
                    syn_persec_exp = (last_k[-1] + average_delta) if (last_k[-1] + average_delta) > 0 else 0

                    flood = 0
                # print("!!! FLOOD ALERT !!!")
            elif(flood == 1):
                # margin_on_error = 1+(2*a)
                last_k.pop(0)
                last_k.append(syn_count0_dec_diff)
                # print(last_k)
                # syn_count0_dec_prev = syn_count0_dec
                flood = 0
            else:
                # if (e_ratio<1+a):
                margin_on_error = 1+a
                last_k.pop(0)
                last_k.append(syn_count0_dec_diff)
                # print(last_k)
                # syn_count0_dec_prev = syn_count0_dec

                deltas = [last_k[i+1] - last_k[i] for i in range(k - 1)]
                average_delta= sum(deltas) / len(deltas)
                syn_persec_exp = (last_k[-1] + average_delta) if (last_k[-1] + average_delta) > 0 else 0

                flood = 0
                # else:
                #     # margin_on_error = 1+a
                #     last_k.pop(-1)
                #     last_k.append(syn_count0_dec_diff)
                #     deltas = [last_k[i+1] - last_k[i] for i in range(k - 1)]
                #     average_delta= sum(deltas) / len(deltas)
                #     syn_persec_exp = (last_k[-1] + average_delta) if (last_k[-1] + average_delta) > 0 else 0

                #     flood = 0

            #minimal f
            abs_e.append(abs(syn_persec_exp-syn_count0_dec_diff))
            # e_func= abs(syn_persec_exp-syn_count0_dec_diff) - betta*k - 1/a

            file.write(f"{iter} {a} {k} {syn_count0_dec_diff} {syn_persec_exp} {allow_count} {e_ratio} {flood}\n")
            # print("i:", iter, "a:", a, "k:", k, "e_ratio:",e_ratio)

            # #next prediction
            # deltas = [last_k[i+1] - last_k[i] for i in range(k - 1)]
            # average_delta= sum(deltas) / len(deltas)
            # syn_persec_exp = (last_k[-1] + average_delta) if (last_k[-1] + average_delta) > 0 else 0
        # print("++++++++++++++++++++++++++++++++++++++++++++++++")
        # time.sleep(1/sps)

    MAE = sum(abs_e) / len(abs_e) + betta*k - 1/a + gamma*FP
    return MAE, FP, train

def sliding_window_mae(params, x, betta=10, gamma=20, lower_bound_allow=10000):
    # Extract parameters
    a = params[0]
    k = int(round(params[1]))
    global max_allowed
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

            if syn_persec_exp > max_allowed:
                max_allowed = syn_persec_exp

    if not abs_e:
        return float('inf')

    # Cost function: MAE + penalty for sensitivity
    mae = sum(abs_e) / len(abs_e) + betta*k - 1/a + gamma*FP
    return mae

def get_a_k (train):
    x = train
    global max_allowed
    max_allowed = 0
    # Define bounds for a and k for global optimization
    bounds = [(0.01, 0.99), (3, 10)]  # a in (0,1), k in [4,50]
    result_de = differential_evolution(func=sliding_window_mae,bounds=bounds,args=(x,),strategy='best1bin',maxiter=100,popsize=15,tol=1e-6,mutation=(0.5, 1),recombination=0.7,seed=42)
    optimized_mae_de = result_de.fun
    optimal_a_de, optimal_k_de = result_de.x[0], int(round(result_de.x[1]))
    # print(optimized_mae_de, optimal_a_de, optimal_k_de)
    # if optimal_a_de <0.1:
    return optimal_a_de, optimal_k_de

def get_chunks(opt_rate,trace):
    with open(trace, "r") as file:
        data = [int(line.strip()) for line in file]
    chunks = [data[i:i + opt_rate] for i in range(0, len(data), opt_rate)]
    print("Start: ----------------------------------",len(chunks))
    time.sleep(2)
    return chunks, data

trace = "day_flood_20240619_12.txt"
opt_rate = 900
#initial a and k
k = 7
a = 0.29271215413236695

fp_total = 0
with open("out.txt", "w") as file:

    chunks, data = get_chunks(opt_rate,trace)

    for i in range(len(chunks)):
        MAE, FP, train = get_mae(chunks[i],k,a)
        fp_total = fp_total + FP

        print("------------------",len(train))
        if len(train) > 2:
        # if i not in [45]: #correction
            a, k = get_a_k(train)
            a = a + 0.4

        else:
            print("SKIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIP")

        print(i, "MAE:", MAE, "FP", FP, "train", len(train),"a",a,"k",k)

    acc = (1-(fp_total/len(data)))*100 
    print('opt_rate',opt_rate,'total detections:', len(data), 'total FP', fp_total, 'accuracy', acc)

# trace = "day_20240619.txt"
# opt_rate = 900

# fp_total = 0
# with open("out.txt", "w") as file:

#     chunks, data = get_chunks(opt_rate,trace)

#     for i in range(len(chunks)):

#         a, k = get_a_k(chunks[i])

#         MAE, FP, train = get_mae(chunks[i],k,a)
#         fp_total = fp_total + FP

#         print(i, "MAE:", MAE, "FP", FP, "train", len(train),"a",a,"k",k)

#     acc = (1-(fp_total/len(data)))*100 
#     print('opt_rate',opt_rate,'total detections:', len(data), 'total FP', fp_total, 'accuracy', acc)

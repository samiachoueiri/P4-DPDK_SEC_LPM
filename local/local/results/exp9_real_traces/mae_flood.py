import time

with open("night_flood.txt", "r") as file:
    x = [int(line.strip()) for line in file]

print(x)



#constants
k = 8
a = 0.3416797172102245
betta = 10
gamma = 20

#declarations
iter = -1
prediction = False
lower_bound_allow = 10000 #allow at least 10000 pkts per sec
margin_on_error = 1+a #allow 20% more pkts
last_k = []
abs_e = []
sps = 1
FP = 0
TP = 0
flood = 0

with open("test_flood.txt", "w") as file:

    while iter < len(x) -1:
        iter +=1
        allow_count = 4000000000
        syn_count0_dec_diff = x[iter]

        if(len(last_k)<k):
            last_k.append(syn_count0_dec_diff)
            print("fill window:" , last_k)

        elif (len(last_k)==k and prediction == False):
            last_k.pop(0)
            last_k.append(syn_count0_dec_diff)

            deltas = [last_k[i+1] - last_k[i] for i in range(k - 1)]
            average_delta= sum(deltas) / len(deltas)
            syn_persec_exp = last_k[-1] + average_delta
            prediction = True

            print("first prediction:",last_k, syn_persec_exp)

        else:
            print("predicted:",syn_persec_exp,"VS. actual:",syn_count0_dec_diff)
            allow_count = max(margin_on_error*syn_persec_exp,lower_bound_allow)
            e_ratio = syn_persec_exp / syn_count0_dec_diff if syn_count0_dec_diff != 0 else float('inf')
            
            if (e_ratio<1-a):
                flood = 1
                print("!!! FLOOD ALERT !!!")
            elif(flood == 1):
                # margin_on_error = 1+(2*a)
                last_k.pop(0)
                last_k.append(syn_count0_dec_diff)
                print(last_k)
                # syn_count0_dec_prev = syn_count0_dec
                flood = 0
            else:
                margin_on_error = 1+a
                last_k.pop(0)
                last_k.append(syn_count0_dec_diff)
                print(last_k)
                # syn_count0_dec_prev = syn_count0_dec

                deltas = [last_k[i+1] - last_k[i] for i in range(k - 1)]
                average_delta= sum(deltas) / len(deltas)
                syn_persec_exp = (last_k[-1] + average_delta) if (last_k[-1] + average_delta) > 0 else 0

                flood = 0





            # print("predicted:",syn_persec_exp,"VS. actual:",syn_count0_dec_diff)

            # last_k.pop(0)
            # last_k.append(syn_count0_dec_diff)

            # allow_count = max(margin_on_error*syn_persec_exp,lower_bound_allow)
            # e_ratio = syn_persec_exp / syn_count0_dec_diff if syn_count0_dec_diff != 0 else float('inf')
            
            # if e_ratio < 1-a:
            #     FP+=1
            #     flood = 1
            # else:
            #     TP+=1
            #     flood = 0
            
            #minimal f
            abs_e.append(abs(syn_persec_exp-syn_count0_dec_diff))
            # e_func= abs(syn_persec_exp-syn_count0_dec_diff) - betta*k - 1/a

            file.write(f"{iter} {a} {k} {syn_count0_dec_diff} {syn_persec_exp} {allow_count} {e_ratio} {flood}\n")
            print("i:", iter, "a:", a, "k:", k, "e_ratio:",e_ratio)

            # #next prediction
            # deltas = [last_k[i+1] - last_k[i] for i in range(k - 1)]
            # average_delta= sum(deltas) / len(deltas)
            # syn_persec_exp = (last_k[-1] + average_delta) if (last_k[-1] + average_delta) > 0 else 0
        print("++++++++++++++++++++++++++++++++++++++++++++++++")
        # time.sleep(1/sps)

MAE = sum(abs_e) / len(abs_e) + betta*k - 1/a + gamma*FP
print("MAE:", MAE, "FP", FP)
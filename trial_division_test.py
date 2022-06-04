import math as m

def trial_division_test(p):
    k = 2 #лічильник
    k_stop = int(m.sqrt(p))
    while k_stop >= k:
        if p % k == 0:
            return "число складене"
        if p % k != 0:
            k += 1
    return "число просте"
        
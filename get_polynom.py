# на вход:
# множество М (состоящее из последовательности коэффициентов alfa)
#
#
# на выход:
# последовательность вычислений полинома
#
from itertools import * 

alfa = "α"

def mod2Conc(a, b):
    conc = str(int(a) + int(b))
    ret = ""
    for i in range(len(conc)): # bruh
        ret += str(int(conc[i])%2)
    return int(ret)

def format_bin_int(val, min_len):
    ret = str(val)
    if len(ret)<min_len:
        for i in range(min_len - len(ret)):
            ret = "0" + ret
    return ret

def cut_last_symbol(str):
    return str[:-1]

def print_wierd_alfa_1(tmp_combinations, write_alfa=True):
    # ?
    ret = "="
    x_pow = len(tmp_combinations)-1
    for block in tmp_combinations:
        ret+= "(" if len(block)>1 else ""
        for alfa_concat in block:
            for alfa_pow in alfa_concat:
                ret += alfa + "^" if write_alfa else ""
                ret += str(alfa_pow)+"*"
            ret = cut_last_symbol(ret)
            ret += "+"
        ret = cut_last_symbol(ret)
        ret+= ")" if len(block)>1 else ""
        ret += "x^" + str(x_pow) if x_pow > 0 else ""
        ret += "+"
        x_pow-=1
    ret = cut_last_symbol(ret)
    print(ret)
    pass

def optimize_combinations(tmp_combinations):
    ret = [0] * len(tmp_combinations)
    i = 0
    for block in tmp_combinations:
        tmp_block = [0]*len(block)
        j = 0
        for chunk in block:
            tmp_sum = 0
            for num in chunk:
                tmp_sum += num
            tmp_block[j] = [tmp_sum]
            j += 1
        ret[i] = tmp_block
        i += 1
    return ret


def mod_combinations(tmp_combinations, val):
    ret = tmp_combinations.copy()
    for i in range(len(tmp_combinations)):
        for j in range(len(tmp_combinations[i])):
            ret[i][j][0] = tmp_combinations[i][j][0]%val
    return ret

def apply_pow_rendered(tmp_combinations, pow_koeffs_rendered, min_len):
    ret = tmp_combinations.copy()
    for i in range(len(tmp_combinations)):
        for j in range(len(tmp_combinations[i])):
            ret[i][j][0] = format_bin_int(pow_koeffs_rendered[tmp_combinations[i][j][0]], min_len)
    return ret

def get_final_polynom(tmp_data):
    ret = ['0']* len(tmp_data)
    for i in range(len(tmp_data)):
        tmp_sum = 0
        for item in tmp_data[i]:
            tmp_sum = mod2Conc(tmp_sum, item[0])
        ret[i] = [[tmp_sum]]
    return ret
################################################################

#
multi_M = [3, 6, 12, 17, 24]
#a = combinations(multi_M, 4)
#print(list(a))

tmp_combinations = [0]* (len(multi_M)+1)
for i in range(len(multi_M)):
    tmp_combinations[i] = list(combinations(multi_M, i))
tmp_combinations[len(multi_M)] = [multi_M]
print_wierd_alfa_1(tmp_combinations)
#
#
tmp_optimized = optimize_combinations(tmp_combinations)
print_wierd_alfa_1(tmp_optimized)
#
#
tmp_mod = mod_combinations(tmp_optimized, 31)
print_wierd_alfa_1(tmp_mod)
#
#
pow_koeffs_rendered = [
    1, 
    10, 
    100,
    1000,
    1101,
    111,
    1110,
    1, 
    10, 
    100,
    1000,
    1101,
    111,
    1110,
    1, 
    10, 
    100,
    1000,
    1101,
    111,
    1110,
    1, 
    10, 
    100,
    1000,
    1101,
    111,
    1110,
    1, 
    10, 
    100,
    1000,
]
tmp_pow = apply_pow_rendered(tmp_mod, pow_koeffs_rendered, 5)
print_wierd_alfa_1(tmp_pow, False)
#
#
polynom = get_final_polynom(tmp_pow)
print_wierd_alfa_1(polynom, False)
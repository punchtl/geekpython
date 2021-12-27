from functools import reduce
new_list = [i for i in range(100,1001) if i % 2 == 0]

def new_func(prev_i, i):
    return prev_i * i
print(reduce(new_func, new_list))
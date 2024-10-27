def minimal(int_list):
    smallest_num = min(int_list)
    return smallest_num

def maximum(int_list):
    biggest_num = max(int_list)
    return biggest_num

def len_list(int_list):
    len_num = len(int_list)
    return len_num

def summary(int_list):
    sum_num = sum(int_list)
    return sum_num

def sorted_list(int_list):
    sorted_num = sorted(int_list)
    return sorted_num

def apply_all_func(int_list, *function):
    result = {}
    for func in function:
        result_func = func(int_list)
        result[func.__name__] = result_func
    return result


print(apply_all_func([6, 20, 15, 9], minimal, maximum))
print(apply_all_func([6, 20, 15, 9], len_list, summary, sorted_list))


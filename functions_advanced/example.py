def some_func(*args):
    args_list = list(args)
    for i in range(len(args_list)):
        if i % 2 == 0:
            args_list[i] += 100
    return args_list


print(some_func(1, 2, 3))
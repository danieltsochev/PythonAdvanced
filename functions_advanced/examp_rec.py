def daniel(x):
    if x == 1:
        return f"good job daniel!: {x}"
    result = daniel(x - 1)
    y = x
    return result


print(daniel(5))
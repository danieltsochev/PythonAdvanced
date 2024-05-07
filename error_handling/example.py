try:
    text = input()
    time = int(input())

    print(time * text)
except ValueError:
    print("time must be an integer")

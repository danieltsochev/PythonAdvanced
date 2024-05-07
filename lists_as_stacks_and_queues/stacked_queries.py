stack_of_numbers = []

result_stack = []

count_of_queries = int(input())

for _ in range(count_of_queries):
    current_query = input()

    if current_query.startswith("2"):
        if len(stack_of_numbers) <= 0:
            continue
        stack_of_numbers.pop()

    elif current_query.startswith("3"):
        if len(stack_of_numbers) <= 0:
            continue
        print(max(stack_of_numbers))

    elif current_query.startswith("4"):
        if len(stack_of_numbers) <= 0:
            continue
        print(min(stack_of_numbers))

    elif current_query.startswith("1"):
        query_needed = current_query.split()
        _, number = query_needed
        stack_of_numbers.append(int(number))

while stack_of_numbers:
    result_stack.append(str(stack_of_numbers.pop()))

print(', '.join(result_stack))


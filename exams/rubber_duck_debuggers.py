from collections import deque

task_time = deque([int(x) for x in input().split()])
number_of_tasks = [int(x) for x in input().split()]

darth_vader_ducky = range(0, 61)
thor_ducky = range(61, 121)
big_blue_rubber_ducky = range(121, 181)
small_yellow_rubber_ducky = range(181, 241)

d_v_d_count = 0
t_d_count = 0
b_b_r_d_count = 0
s_y_r_d_count = 0

while task_time and number_of_tasks:

    current_time = task_time.popleft()
    current_task = number_of_tasks.pop()
    result = current_time * current_task

    if result in darth_vader_ducky:
        d_v_d_count += 1

    elif result in thor_ducky:
        t_d_count += 1

    elif result in big_blue_rubber_ducky:
        b_b_r_d_count += 1

    elif result in small_yellow_rubber_ducky:
        s_y_r_d_count += 1

    elif result > 240:
        current_task -= 2
        number_of_tasks.append(current_task)
        task_time.append(current_time)

print(f"Congratulations, all tasks have been completed! Rubber ducks rewarded:")
print(f"Darth Vader Ducky: {d_v_d_count}")
print(f"Thor Ducky: {t_d_count}")
print(f"Big Blue Rubber Ducky: {b_b_r_d_count}")
print(f"Small Yellow Rubber Ducky: {s_y_r_d_count}")



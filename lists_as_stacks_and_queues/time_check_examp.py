from collections import deque
import time

stat_time = time.time()

numbers = deque([1, 2, 3, 4])

numbers.popleft()

print(numbers)

print("--- %s seconds ---" % (time.time() - stat_time))

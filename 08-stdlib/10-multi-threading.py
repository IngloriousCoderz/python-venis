from concurrent.futures import ThreadPoolExecutor
from threading import Thread
import random
import time

numbers = range(1, 5)


# def long_task(name):
#     print(f"Starting task {name}...")
#     delay = random.choice(numbers)
#     time.sleep(delay)
#     print(f"Task {name} done after {delay} seconds.")


# for num in numbers:
#     long_task(num)
# print("All tasks ended.")

# threads = [Thread(target=long_task, args=(num,)) for num in numbers]

# print("Starting threads...")
# for thread in threads:
#     thread.start()
# for thread in threads:
#     thread.join()
# print("All done.")

# results = [None for _ in numbers]


# def long_task(name):
#     print(f"Starting task {name}...")
#     delay = random.choice(numbers)
#     time.sleep(delay)
#     index = name - 1
#     results[index] = name
#     print(f"Task {name} done after {delay} seconds.")


# threads = [Thread(target=long_task, args=(num,)) for num in numbers]

# print("Starting threads...")
# for thread in threads:
#     thread.start()
# for thread in threads:
#     thread.join()
# print("All done.")
# print("Results:", results)


def long_task(name):
    print(f"Starting task {name}...")
    delay = random.choice(numbers)
    time.sleep(delay)
    print(f"Task {name} done after {delay} seconds.")
    return name


# print(long_task('1'))

with ThreadPoolExecutor(max_workers=4) as executor:
    results = executor.map(long_task, numbers)
print("All done.")
print("Results:", list(results))

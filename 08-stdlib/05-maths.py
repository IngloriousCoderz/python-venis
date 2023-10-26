import statistics
import random
import math

22 / 7
math.pi
math.sin(math.pi / 2)  # 1.0
math.log(1024, 2)  # 10.0


random.random()  # floating point between 0 and 1
int(random.random() * 6 + 1)  # die values
random.choice(['apple', 'orange', 'banana'])
random.choice(range(1, 7))
random.randrange(1, 7)
random.sample(range(100), 10)


marks = [7, 7, 8, 6, 9, 7, 5, 6]
statistics.mean(marks)  # 6.875
statistics.median(marks)  # 7.0 (middle value)
statistics.variance(marks)  # 1.55... (spread or dispersion)

# For more complex maths @see https://scipy.org/
# See Anaconda, a scientific Python distribution

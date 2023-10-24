# lists behave as stacks already
stack = [1, 2, 3]
stack.append(4)
stack.pop()

# using lists as queues is slow, use deque
from collections import deque

queue = deque([1, 2, 3])
queue.append(4)
queue.popleft()

list(queue)

import time


nums = [0, 0]

# async def fib(i, delay,  maximum=0):
#     a = b = 1
#     while maximum > a:
#         a, b = b, a + b
#         nums[i] = a
#         await sleep(delay)

class sleep:
    def __init__(self, delay):
        self.delay = delay

    def __await__(self):
        yield self.delay/2
        yield self.delay/2

tasks = [
    # (0, 1, fib(0 ,1/10 ,maximum=1000).__await__()),
    # (0, 2, fib(1 ,1/3 ,maximum=1000).__await__()),
    ]

number = 0
def create_task(task):
    global number
    number += 1

    task = 0, number, task.__await__()
    tasks.append(task)
    return sleep(0) #HACK


def run(task):
    create_task(task)
    current_time = 0
    while tasks:
        tasks.sort()
        task = tasks.pop(0)
        time_task ,number ,iterator = task
        if time_task > current_time:
            time.sleep(time_task - current_time)
            current_time = time_task
        try:
            delay = next(iterator)
        except StopIteration:
            pass
        else:
            task = time_task + delay, number, iterator
            tasks.append(task)

        # print(nums)



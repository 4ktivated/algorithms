def clocker(func):
    def clock(*args):
        import time
        start_time = time.time()
        func(*args)
        print(f"[{time.time() - start_time}]{func.__name__}")
    return clock

@clocker
def main():
    for i in range(0,1000):
        print(i)
main()   
def clocker(func):
    def clock(*args):
        import time
        start_time = time.time()
        func(*args)
        print(f"[{time.time() - start_time}]{func.__name__}")
    return clock
@clocker
def main(i):
    print(i*i)
i = 100
main()   
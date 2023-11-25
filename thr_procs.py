from concurrent.futures import ThreadPoolExecutor
from threading import Thread
import threading
from multiprocessing import Process
import time
import os
cnt = 0

def f_sleep():
    print(f'Поток: {threading.get_ident()} | Процесс: {os.getpid()}')
    time.sleep(1)

def havy_f():
    cnt = 0
    for _ in range(5_000_000_0):
        cnt += 1 
    print(f'Поток: {threading.get_ident()} | Процесс: {os.getpid()}')
    
def func():
    global cnt
    cnt += 1
    print(f'Поток: {threading.get_ident()} | Процесс: {os.getpid()} {cnt}')
start = time.time()



with ThreadPoolExecutor(max_workers=5) as t:
    [t.submit(func) for _ in range(5)]
# th = Thread(target=havy_f)
# th1 = Thread(target=havy_f)
# th.start()
# th1.start()
# th.join()
# th1.join()

print(time.time() - start)
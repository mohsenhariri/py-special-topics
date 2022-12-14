"""
Kernel-level threads
For green threads check asyncio
"""
import threading

from tasks import idle_process
from utility import time_profiler

heavy_process = idle_process


@time_profiler
def run():
    heavy_process(1)
    heavy_process(2)


run()


@time_profiler
def run_with_threads():
    t1 = threading.Thread(target=heavy_process, args=(3,))
    t2 = threading.Thread(target=heavy_process, args=(4,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


run_with_threads()


@time_profiler
def run_with_threads_n(n: int):
    threads = [threading.Thread(target=heavy_process, args=(i,)) for i in range(n)]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]


run_with_threads_n(10)

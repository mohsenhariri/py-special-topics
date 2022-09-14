import multiprocessing

from tasks import idle_process
from utility import time_profiler

heavy_process = idle_process


@time_profiler
def run():
    heavy_process(1)
    heavy_process(2)


run()


@time_profiler
def run_multi():
    p1 = multiprocessing.Process(target=heavy_process, args=(3,))
    p2 = multiprocessing.Process(target=heavy_process, args=(4,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


run_multi()


@time_profiler
def run_multi_n(n: int):
    processes = [
        multiprocessing.Process(target=heavy_process, args=(i,)) for i in range(n)
    ]
    [process.start() for process in processes]
    [process.join() for process in processes]


run_multi_n(10)

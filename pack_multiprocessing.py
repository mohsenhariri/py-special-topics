import multiprocessing
from utility import exec_time, heavy_process


@exec_time
def run():
    heavy_process(1)
    heavy_process(2)


run()


@exec_time
def run_multi():
    p1 = multiprocessing.Process(target=heavy_process, args=(3,))
    p2 = multiprocessing.Process(target=heavy_process, args=(4,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


run_multi()


@exec_time
def run_multi_n(n: int):
    processes = [
        multiprocessing.Process(target=heavy_process, args=(i,)) for i in range(n)
    ]
    [process.start() for process in processes]
    [process.join() for process in processes]


run_multi_n(10)

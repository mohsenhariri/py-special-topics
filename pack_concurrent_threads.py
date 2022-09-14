import concurrent.futures

from tasks import idle_process
from utility import time_profiler

heavy_process = idle_process


@time_profiler
def run_with_concurrent():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        e1 = executor.submit(heavy_process, 1)
        e2 = executor.submit(heavy_process, 2)
        r1 = e1.result()
        r2 = e2.result()
        print([r1, r2])


run_with_concurrent()


@time_profiler
def run_with_concurrent_n(n: int):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executors = [executor.submit(heavy_process, i) for i in range(n)]
        results = [executor.result() for executor in executors]
        print(results)


run_with_concurrent_n(10)


@time_profiler
def run_with_concurrent_resloved(n: int):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executors = [executor.submit(heavy_process, i) for i in range(n)]
        results = [
            resolved_executor.result()
            for resolved_executor in concurrent.futures.as_completed(executors)
        ]
        print(results)


run_with_concurrent_resloved(10)


@time_profiler
def run_with_concurrent_map(n: int):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(heavy_process, [i for i in range(n)])


run_with_concurrent_map(10)

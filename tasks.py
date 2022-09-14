import copy
import io
import sys
import time

from utility import download

sys.setrecursionlimit(80001)

__all__ = [
    "cpu_bound_fib",
    "cpu_bound_prime",
    "cpu_memory_bound",
    "network_bound",
    "idle_process",
]


def cpu_bound_fib(n: int) -> int:
    """Recursive Fibonacci calculator.
    Args:
        n (int): integer input should be greater than 1
    Returns:
        int:  nth Fibonacci number.
    """
    return 1 if n == 1 or n == 2 else cpu_bound_fib(n - 1) + cpu_bound_fib(n - 2)


def cpu_bound_prime(n: int) -> int:
    """A bad prime finder!
    Args:
        n (int): The closest prime to n will be returned.
    Returns:
        int: Closet prime to input n.
    """
    primes_less_than_n = [2]
    x = 2
    while x < n:
        is_prime = True
        for prime in primes_less_than_n:
            if x % prime == 0:
                is_prime = False
                break
        if is_prime == True:
            primes_less_than_n.append(x)
        x += 1

    return primes_less_than_n[-1]


def network_bound() -> None:
    download(
        "https://images-assets.nasa.gov/video/Evolution_of_Galaxies_H264/Evolution_of_Galaxies_H264~orig.mp4"
    )


def cpu_mem_net_bound(n: int) -> bytes:
    download(
        "https://images-assets.nasa.gov/video/Evolution_of_Galaxies_H264/Evolution_of_Galaxies_H264~orig.mp4"
    )
    with open("./download/Evolution_of_Galaxies_H264_orig.mp4", "br") as fp:

        fb = io.BufferedReader(fp)
        content = fb.read()

        chromish_memory_devourer = bytes()
        for _ in range(n):
            d = copy.deepcopy(content)
            chromish_memory_devourer += d

        return chromish_memory_devourer


def idle_process(caller_id: int) -> int:
    time.sleep(1)
    print(f"{caller_id} was done.")
    return caller_id

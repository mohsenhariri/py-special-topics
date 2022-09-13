import time


def exec_time(f):
    def wrap(*args, **kwargs):
        begin = time.perf_counter()
        wrap_returned_value = f(*args, **kwargs)
        end = time.perf_counter()
        print(f"Running time: {round(end - begin, 3)} time.")
        return wrap_returned_value

    return wrap


def heavy_process(caller_id: int):
    time.sleep(1)
    print(f"{caller_id} was done.")
    return caller_id

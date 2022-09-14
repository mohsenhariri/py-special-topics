import time
import tracemalloc
import urllib.request
import uuid
from pathlib import Path
from shutil import copyfileobj


def time_profiler(f):
    def wrap(*args, **kwargs):
        begin = time.perf_counter()
        wrap_returned_value = f(*args, **kwargs)
        end = time.perf_counter()
        print(f"Running time: {round(end - begin, 3)} time.")
        return wrap_returned_value

    return wrap


def memory_profiler(f):
    def wrap(*args, **kwargs):
        tracemalloc.start()
        wrap_returned_value = f(*args, **kwargs)
        snapshot = tracemalloc.take_snapshot()
        stats = snapshot.statistics(key_type="lineno", cumulative=True)
        print(f"Allocated memory: {stats[0]}")
        return wrap_returned_value

    return wrap


def download(url: str):

    download_path = Path(r"./download")
    if not download_path.exists():
        download_path.mkdir()

    download_path = download_path / f"{uuid.uuid4()}.jpg"
    try:
        with urllib.request.urlopen(url) as stream, open(download_path, "wb") as fp:
            copyfileobj(stream, fp)
    except (urllib.error.URLError, urllib.error.HTTPError):
        print("An error was occured.")
    else:
        print("Downloaded successfully.")

import concurrent.futures

from utility import download, exec_time

urls = [
    "https://images.unsplash.com/photo-1551214359-b81f66a605b1",
    "https://images.unsplash.com/photo-1552959988-b94b76838365",
    "https://images.unsplash.com/photo-1545548171-37a54e5c1ea6",
    "https://images.unsplash.com/photo-1542372177-002ea9732b17",
    "https://images.unsplash.com/photo-1541562232579-512a21360020",
    "https://images.unsplash.com/photo-1620336655055-088d06e36bf0",
    "https://images.unsplash.com/photo-1528360983277-13d401cdc186",
    "https://images.unsplash.com/photo-1611457194403-d3aca4cf9d11",
    "https://images.unsplash.com/photo-1552959988-b94b76838365",
]


@exec_time
def run():
    for url in urls:
        download(url)


run()


@exec_time
def run_thread():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download, urls)


run_thread()


@exec_time
def run_process():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(download, urls)


run_process()

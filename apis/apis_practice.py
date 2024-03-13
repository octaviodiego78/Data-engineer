import requests
from urllib import request
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

urls = ['https://jsonplaceholder.typicode.com/posts'] * 10  # Simplified to 10 identical URLs

def get_response(url):
    """
    Get response from the provided URL
    """
    with request.urlopen(url) as connection:
        response = connection.read().decode('utf-8')
        return response
def main():
    # Synchronous
    times = []
    for _ in range(5):
        t0 = time.time()
        for url in urls:
            get_response(url)
        times.append(time.time() - t0)
    print("Synchronous Average:", sum(times) / len(times))


    # ThreadPoolExecutor
    times = []
    for _ in range(5):
        t0 = time.time()
        with ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(get_response, urls)
        times.append(time.time() - t0)
    print("ThreadPoolExecutor Average:", sum(times) / len(times))


    # ProcessPoolExecutor
    times = []
    for _ in range(5):
        t0 = time.time()
        with ProcessPoolExecutor(max_workers=5) as executor:
            executor.map(get_response, urls)
        times.append(time.time() - t0)
    print("ProcessPoolExecutor Average:", sum(times) / len(times))

    return None

if __name__ == "__main__":
    main()


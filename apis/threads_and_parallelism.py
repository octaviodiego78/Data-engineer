import requests
from  urllib import  request
import json
from concurrent.futures import ThreadPoolExecutor
import time




def return_response(url):
    t0 = time.time()
    with request.urlopen(url) as connection:
        response = connection.read().decode('utf-8')

    print(f"Request {url[-1]} took {time.time() - t0} seconds")
    return response

urls = [
    'https://jsonplaceholder.typicode.com/posts/1',
    'https://jsonplaceholder.typicode.com/posts/2',
    'https://jsonplaceholder.typicode.com/posts/3',
    'https://jsonplaceholder.typicode.com/posts/4',
    'https://jsonplaceholder.typicode.com/posts/5'
]



responses = []
t0 = time.time()
print("Without ThreadPoolExecutor")
for url in urls:
    responses.append(return_response(url))
print(f"Total time taken: {time.time() - t0} seconds")
print("")

print("Using ThreadPoolExecutor")
t0 = time.time()
with ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(return_response, urls)
print(f"Total time taken: {time.time() - t0} seconds")
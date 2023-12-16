import logging
import os
import threading
import time
from string import ascii_letters
from random import randint, choice, choices

import docker
import requests
from fastapi import HTTPException


def generate_text():
    ip_a = "{}.{}.{}.{}".format(randint(0, 255), randint(0, 255), randint(0, 255), randint(0, 255))

    methods_list = ["GET", "HEAD", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", "TRACE"]
    http_method = choice(methods_list)

    uri = ''
    for index in range(randint(1, 3)):
        uri += '/' + ''.join(choices(ascii_letters, k=randint(3, 7)))

    http_status_code = randint(200, 300)

    return ip_a + ' ' + http_method + ' ' + uri + ' ' + str(http_status_code)


def make_post_request(url_src, data_src):
    try:
        response = requests.post(url_src, json=data_src)
        if response.status_code == 201:
            print("Лог сохранeн")
    except requests.RequestException as e:
        print(e)
        raise HTTPException(status_code=418, detail="Что-то пошло не так")


THREADS = os.environ["THREADS"]
DELAY = os.environ["DELAY"]

# client = docker.from_env()
# container = client.containers.get("mywebapi")
# container_info = container.attrs
#
# if 'NetworkSettings' in container_info and 'IPAddress' in container_info:
#     ip_addr = container_info['NetworkSettings']['IPAddress']
# else:
#     ip_addr = None
#
# print(ip_addr)
#
# if ip_addr:
#     url = f'http://{ip_addr}:8000/api/data'
# else:
#     url = f'http://localhost:8000/api/data'

url = 'http://177.77.0.3:8000/api/data'
# url = f'http://localhost:8000/api/data'

for i in range(int(THREADS)):
    time.sleep(randint(0, int(DELAY)) / 1000)

    gen_data = generate_text()
    data = {"log": f"{gen_data}"}

    logging.basicConfig(filename='client.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info(f"URL: {url} - Text: '{gen_data}'")

    threading.Thread(target=make_post_request(url, data)).start()

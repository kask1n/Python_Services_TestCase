import logging
import os
import threading
import time
from string import ascii_letters
from random import randint, choice, choices

import requests
from fastapi import HTTPException


def generate_text():
    ip_address = "{}.{}.{}.{}".format(randint(0, 255), randint(0, 255), randint(0, 255), randint(0, 255))

    methods_list = ["GET", "HEAD", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", "TRACE"]
    http_method = choice(methods_list)

    uri = ''
    for index in range(randint(1, 3)):
        uri += '/' + ''.join(choices(ascii_letters, k=randint(3, 7)))

    http_status_code = randint(200, 300)

    return ip_address + ' ' + http_method + ' ' + uri + ' ' + str(http_status_code)


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

url = 'http://127.0.0.1:8000/api/data'

for i in range(int(THREADS)):
    time.sleep(randint(0, int(DELAY)) / 1000)

    gen_data = generate_text()
    data = {"log": f"{gen_data}"}

    logging.basicConfig(filename='client.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info(f"URL: {url} - Text: '{gen_data}'")

    threading.Thread(target=make_post_request(url, data)).start()

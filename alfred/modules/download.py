import threading
import requests
import queue


def download(url):
    return_value = queue.Queue()
    create_thread(url, return_value)
    return return_value.get()


def get_respone(url, return_value):
    try:
        response = requests.get(url)
        return_value.put(response.text)
    except requests.exceptions.ConnectionError:
        return_value.put(0)


def create_thread(url, return_value):
    thread = threading.Thread(target=get_respone, args=(url, return_value))
    thread.start()
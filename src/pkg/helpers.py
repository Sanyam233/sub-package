import requests as re


def func():
    response = re.get("https://jsonplaceholder.typicode.com/todos/1")
    return response.json()

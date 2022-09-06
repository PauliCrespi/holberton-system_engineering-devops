#!/usr/bin/python3
"""task 3"""

import json
import requests

if __name__ == "__main__":
    todos = []
    dictionary = {}
    api_url = "https://jsonplaceholder.typicode.com/users"
    resp_u = requests.get(api_url).json()
    for user in resp_u:
        todos = []
        idd = user.get('id')
        api_t = "https://jsonplaceholder.typicode.com/todos"
        resp_t = requests.get(api_t, params={"userId": idd}).json()
        item = ""
        for item in resp_t:
            list_t = {}
            list_t["task"] = item.get('title')
            list_t["completed"] = item.get('completed')
            list_t["username"] = user.get('username')
            todos.append(list_t)
        dictionary[idd] = todos
    with open('todo_all_employees.json', 'w+') as f:
        json.dump(dictionary, f)

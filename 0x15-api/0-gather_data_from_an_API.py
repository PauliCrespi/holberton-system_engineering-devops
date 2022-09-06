#!/usr/bin/python3
"""task 0"""

import requests
from sys import argv

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    api_u = api_url + "users/" + str(argv[1])
    api_t = api_url + "todos"
    resp_u = requests.get(api_u)
    resp_t = requests.get(api_t, params={"userId": argv[1]}).json()
    EMPLOYEE_NAME = resp_u.json()["name"]
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    for item in resp_t:
        if item.get('completed') is True:
            NUMBER_OF_DONE_TASKS += 1
        TOTAL_NUMBER_OF_TASKS += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for item in resp_t:
        if item.get('completed') is True:
            print("\t {}".format(item.get('title')))

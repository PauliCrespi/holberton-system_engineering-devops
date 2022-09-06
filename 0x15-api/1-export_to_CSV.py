#!/usr/bin/python3
"""task 1"""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    fname = argv[1] + ".csv"
    f = open(fname, 'w+')
    writer = csv.writer(f, quotechar='"', quoting=csv.QUOTE_ALL)
    api_url = "https://jsonplaceholder.typicode.com/users/" + str(argv[1])
    api_t = "https://jsonplaceholder.typicode.com/todos"
    resp_t = requests.get(api_t, params={"userId": argv[1]}).json()
    resp_u = requests.get(api_url)
    idd = argv[1]
    uname = resp_u.json()["username"]
    for item in resp_t:
        status = str(item.get('completed'))
        title = item.get('title')
        data = [idd, uname, status, title]
        writer.writerow(data)
    f.close()

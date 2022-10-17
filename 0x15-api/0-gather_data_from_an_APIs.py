#!/usr/bin/python3
import requests
import sys

url = "https://jsonplaceholder.typicode.com/"
user = requests.get(url + "users/{}".format(sys.argv[1]))
user_data = user.json()
todos = requests.get(url + "todos", params={"userId": user_data["id"]}).json()


def counter_todo():
    counter = 0
    complete = []
    for element in todos:
        if element["completed"]:
            complete.append(element["title"])
            counter += 1
    return {"len_complet": counter, "title": complete}


if __name__ == "__main__":
    len_task_done = counter_todo()["len_complet"]
    title_todo = counter_todo()["title"]
    print("Employee {} is done with tasks({}/{}):".format(
        user_data.get("name"), len_task_done, len(todos)))
    [print("\t {}".format(c)) for c in title_todo]

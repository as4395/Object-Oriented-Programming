import requests as rq

people_in_space = rq.get("https://api.open-notify.org/astros.json").json()
print(people_in_space)

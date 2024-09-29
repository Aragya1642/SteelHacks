import requests

params = [{
    "description" : "I am looking for engineering events"
        }]

sites = ["getObjects", "getCalendarEvents", "getTitles"]

print(requests.post(r"http://127.0.0.1:5000/getObjects", data=params[0]).text)

for i in sites:
    for j in params:
        print(requests.post(r"http://127.0.0.1:5000/"+i, data=j).text)
        print(requests.get(r"http://127.0.0.1:5000/"+i, params=j).text)

import requests
import json
import csv


def fetch_data():

    response = requests.get("https://api.github.com/search/repositories?q=is:public+language:Python&forks%3E=200")

    print("Status Code of Response from API : {}".format(response.status_code))

    if response.status_code != 200:
        print(response.text)
    else:
        def jprint(obj):
            # create a formatted string of Python JSON object
            text = json.dumps(obj, sort_keys=True, indent=4)
            fo = open("g_data.json", "w")
            fo.write(text)
            fo.close()

        jprint(response.json())

    with open('g_data.json', 'r') as fo:
        data = json.load(fo)

    file = open('git_data.csv', 'w', newline='')
    writer = csv.writer(file)
    writer.writerow(["Name", "Description", "Watchers_Count", "Stargazers_Count", "Forks_Count", "HTML_URL"])

    for value in data['items']:
        temp = value['stargazers_count']

        if temp > 2000:
            a = (value['name'])
            b = (value['description'])
            c = (value['watchers_count'])
            d = (value['stargazers_count'])
            e = (value['forks_count'])
            f = (value['html_url'])
            writer.writerow([a, b, c, d, e, f])

    file.close()

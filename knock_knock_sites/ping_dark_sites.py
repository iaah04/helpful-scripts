import requests
import json
import uuid

session = requests.session()
session.proxies = {}
session.proxies["http"] = "socks5h://localhost:9050"
session.proxies["https"] = "socks5h://localhost:9050"

with open(
    "list_of_dark_sites_72611697-b17f-4db7-b2e1-043e13bc9468.json", "r"
) as json_file:
    links = json.load(json_file)

results = []

for link in links:
    try:
        response = session.get(link)
        if response.status_code == 200:
            print(f"{link} is accessible.")
        else:
            print(f"{link} returned a status code: {response.status_code}")
        results.append({"link": link, "status": response.status_code})
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

file_name = f"list_of_dark_statuses_{uuid.uuid4()}.json"
with open(file_name, "w") as json_file:
    json.dump(results, json_file, indent=4)

print(f"Finished: {file_name}")

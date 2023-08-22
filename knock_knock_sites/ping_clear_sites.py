import requests
import json
import uuid

with open(
    "list_of_clear_sites_4e8752e3-7066-44cb-b42c-7e40bd43d9e8.json", "r"
) as json_file:
    links = json.load(json_file)

results = []

for link in links:
    try:
        response = requests.get(link, timeout=10)
        print(f"{link} : {response.status_code}")
        results.append({"link": link, "status": response.status_code})
    except requests.Timeout:
        print(f"Timeout occurred for: {link}")
        results.append({"link": link, "status": 408})
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

file_name = f"list_of_clear_statuses_{uuid.uuid4()}.json"
with open(file_name, "w") as json_file:
    json.dump(results, json_file, indent=4)

print(f"Finished: {file_name}")

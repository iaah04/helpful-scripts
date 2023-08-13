import requests
import json
import uuid

with open("list_of_clear_sites_45abe624-69ec-4934-8ebb-f7fb32ce6080.json", "r") as json_file:
    links = json.load(json_file)

results = []

for link in links:
    try:
        response = requests.get(link)
        if response.status_code == 200:
            print(f"{link} is accessible.")
        else:
            print(f"{link} returned a status code: {response.status_code}")
        results.append({"link": link, "status": response.status_code})
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

file_name = f"list_of_statuses_{uuid.uuid4()}.json"
with open(file_name, "w") as json_file:
    json.dump(results, json_file, indent=4)

print(f"Finished: {file_name}")

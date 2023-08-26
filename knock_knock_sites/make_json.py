import json
import uuid
import requests
import re

url = "WRITE_HERE"
substring_to_exclude = "WRITE_HERE"

response = requests.get(url)
pattern = r'<a\s+(?:[^>]*?\s+)?href="([^"]*)"'
links = re.findall(pattern, response.text)
filtered_links = [link for link in links if substring_to_exclude not in link]

file_name = f"list_of_links_{uuid.uuid4()}.json"
with open(file_name, "w") as json_file:
    json.dump(filtered_links, json_file, indent=4)

print(f"Finished: {file_name}")
import json
import uuid
import requests
import re

url = "https://mrakopedia.net/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%BD%D1%8B%D1%85_%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D0%BD%D0%B5%D1%82-%D1%81%D0%B0%D0%B9%D1%82%D0%BE%D0%B2"
substring_to_exclude = "mrakopedia"

response = requests.get(url)
pattern = r'<a\s+(?:[^>]*?\s+)?href="([^"]*)"'
links = re.findall(pattern, response.text)
filtered_links = [link for link in links if substring_to_exclude not in link]

file_name = f"list_of_links_{uuid.uuid4()}.json"
with open(file_name, "w") as json_file:
    json.dump(filtered_links, json_file, indent=4)

print(f"Finished: {file_name}")
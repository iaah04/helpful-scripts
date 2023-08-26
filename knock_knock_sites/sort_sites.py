import requests
import json
import uuid
import re

substring_to_exclude = "onion"

with open("WRITE_HERE", "r") as json_file:
    links = json.load(json_file)

dark_links = [link for link in links if substring_to_exclude in link]
clear_links = [link for link in links if substring_to_exclude not in link]

dark_name = f"list_of_dark_sites_{uuid.uuid4()}.json"
with open(dark_name, "w") as json_file:
    json.dump(dark_links, json_file, indent=4)

clear_name = f"list_of_clear_sites_{uuid.uuid4()}.json"
with open(clear_name, "w") as json_file:
    json.dump(clear_links, json_file, indent=4)


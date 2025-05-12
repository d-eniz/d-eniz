import json
import urllib.request
import os

script_dir = os.path.dirname(__file__)
output_path = os.path.join(script_dir, "download-badge.json")


STATS_URL = "https://raw.githubusercontent.com/obsidianmd/obsidian-releases/master/community-plugin-stats.json"
PLUGIN_ID = "jupymd"

with urllib.request.urlopen(STATS_URL) as response:
    stats = json.load(response)

downloads = stats.get(PLUGIN_ID, {}).get("downloads", 0)

badge = {
    "schemaVersion": 1,
    "label": "downloads",
    "message": str(downloads),
    "color": "573E7A",
}

with open(output_path, "w") as f:
    json.dump(badge, f)

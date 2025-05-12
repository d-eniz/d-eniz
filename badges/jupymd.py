import json
import urllib.request

STATS_URL = "https://raw.githubusercontent.com/obsidianmd/obsidian-releases/master/community-plugin-stats.json"
PLUGIN_ID = "jupymd"

with urllib.request.urlopen(STATS_URL) as response:
    stats = json.load(response)

downloads = stats.get(PLUGIN_ID, {}).get("downloads", 0)

badge = {
    "schemaVersion": 1,
    "label": "downloads",
    "message": str(downloads),
    "color": "573E7A"
}

with open("badges/download-badge.json", "w") as f:
    json.dump(badge, f)

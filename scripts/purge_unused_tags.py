import os
import json
import urllib.request

def req_anki(action, params={}):
    url = "http://127.0.0.1:8765"
    p = json.dumps({"action": action, "version": 6, "params": params}).encode("utf-8")
    try:
        with urllib.request.urlopen(urllib.request.Request(url, data=p, headers={"Content-Type": "application/json"})) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"AnkiConnect Error: {e}")
        return {}

def main():
    tags = req_anki("getTags").get("result", [])
    print(f"Total tags in Anki: {len(tags)}")

    if not tags:
        print("No tags found.")
        return

    # Check clearUnusedTags
    res = req_anki("clearUnusedTags")
    print("clearUnusedTags result:", res)

    # Re-check remaining tags
    remaining_tags = req_anki("getTags").get("result", [])
    print(f"Remaining tags after clearUnusedTags: {len(remaining_tags)}")

if __name__ == "__main__":
    main()

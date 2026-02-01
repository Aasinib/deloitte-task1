import json
from datetime import datetime


def iso_to_millis(iso_time):
    dt = datetime.fromisoformat(iso_time.replace("Z", "+00:00"))
    return int(dt.timestamp() * 1000)


def unify_data(data):
    return {
        "device_id": data.get("deviceId") or data.get("id"),
        "timestamp": (
            data["timestamp"]
            if isinstance(data["timestamp"], int)
            else iso_to_millis(data["timestamp"])
        ),
        "temperature": data.get("temperature") or data.get("temp"),
        "humidity": data.get("humidity")
    }


def load_json(filename):
    with open(filename, "r") as f:
        return json.load(f)


def main():
    data1 = load_json("data-1.json")
    data2 = load_json("data-2.json")

    unified1 = unify_data(data1)
    unified2 = unify_data(data2)

    print("Unified data from data-1.json:")
    print(json.dumps(unified1, indent=2))

    print("\nUnified data from data-2.json:")
    print(json.dumps(unified2, indent=2))


if __name__ == "__main__":
    main()

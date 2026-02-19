import json
import os
from datetime import datetime

STORAGE_FILE = os.path.join("storage", "detections.json")


def save_full_record(image_name, detected_items, description, recipe=None, health_score=None):
    os.makedirs("storage", exist_ok=True)
    if os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, "r") as f:
            try:
                data = json.load(f)
            except:
                data = []
    else:
        data = []

    record = {
        "image": image_name,
        "ingredients": detected_items,
        "description": description,
        "recipe": recipe,
        "health_score": health_score,
        "timestamp": datetime.now().isoformat()
    }

    data.append(record)

    with open(STORAGE_FILE, "w") as f:
        json.dump(data, f, indent=4)

    print("✅ Full record saved successfully.")

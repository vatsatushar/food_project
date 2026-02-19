from app.services.detection_service import detect_ingredients
from app.services.description_service import generate_description

def process_image(image_path):
    detected_items = detect_ingredients(image_path)

    print("\nDetected Ingredients:")
    for item in detected_items:
        print(f"- {item['name']} ({item['confidence']}%)")

    description = generate_description(detected_items)

    print("\nGenerated Description:")
    print(description)

    return description

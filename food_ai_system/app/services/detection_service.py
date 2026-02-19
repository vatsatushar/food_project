from app.models.blip_loader import load_blip
from app.services.groq_service import call_groq
from PIL import Image
import ast


def detect_ingredients(image_path):
    processor, model = load_blip()

    image = Image.open(image_path).convert("RGB")
    inputs = processor(image, return_tensors="pt")
    output = model.generate(**inputs, max_new_tokens=50)

    caption = processor.decode(output[0], skip_special_tokens=True)

    print("BLIP Caption:", caption)
    
    prompt = f"""
You are a food recognition expert.

From the following image description:

"{caption}"

Extract ONLY the edible food items.
Return result strictly as a Python list.
Example:
["milk", "banana"]

If no food, return [].
"""

    response = call_groq(prompt, temperature=0)

    try:
        ingredients = ast.literal_eval(response)
    except:
        ingredients = []

    return [{"name": item.lower(), "confidence": 100} for item in ingredients]

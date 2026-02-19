import ast
from app.services.groq_service import call_groq


def filter_edible_items_ai(detected_items):
    if not detected_items:
        return []

    item_names = [item["name"] for item in detected_items]

    prompt = f"""
You are a food classification expert.

From the following list of detected objects:

{item_names}

Return ONLY the items that are edible food ingredients.
Remove all non-food objects like person, table, cup, chair, etc.

Return output strictly as a Python list.
Example:
["banana", "milk"]
"""

    response = call_groq(prompt, temperature=0)

    try:
        edible_list = ast.literal_eval(response)
        return [item for item in detected_items if item["name"] in edible_list]
    except Exception as e:
        print("Error parsing edible list:", e)
        return []

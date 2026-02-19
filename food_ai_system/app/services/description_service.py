def generate_description(detected_items):
    if not detected_items:
        return "No ingredients detected."

    ingredient_names = [item["name"] for item in detected_items]

    description = (
        f"The image contains the following ingredients: "
        f"{', '.join(ingredient_names)}."
    )

    return description

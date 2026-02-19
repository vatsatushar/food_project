from app.services.groq_service import call_groq
from app.utils.prompts import recipe_prompt

def generate_recipe(ingredients):
    ingredients_str = ", ".join(ingredients)
    prompt = recipe_prompt(ingredients_str)
    return call_groq(prompt, temperature=0.7)

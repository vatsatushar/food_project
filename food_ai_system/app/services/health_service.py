from app.services.groq_service import call_groq
from app.utils.prompts import health_prompt

def generate_health_score(ingredients):
    ingredients_str = ", ".join(ingredients)
    prompt = health_prompt(ingredients_str)
    return call_groq(prompt, temperature=0.3)

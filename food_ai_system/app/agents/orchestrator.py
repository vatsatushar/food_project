from .tavily_agent import search_food_research
from app.services.groq_service import call_groq
from app.utils.prompts import final_agent_prompt


def run_agent_pipeline(ingredients):
    research_raw = search_food_research(ingredients)

    final_prompt = final_agent_prompt(", ".join(ingredients), research_raw)
    final_output = call_groq(final_prompt, temperature=0.5)

    return final_output, None

import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_food_research(ingredients):
    query = f"Latest nutrition research and health benefits of {', '.join(ingredients)}"

    response = client.search(
        query=query,
        search_depth="advanced",
        max_results=3
    )

    summaries = []

    for result in response["results"]:
        summaries.append(result["content"])

    return "\n".join(summaries)

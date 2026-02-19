def final_agent_prompt(ingredients, research_summary):
    return f"""
You are a chef and nutrition evaluator.

Ingredients:
{ingredients}

Research:
{research_summary}

Your task:

1. Suggest the best simple recipe using the ingredients.
2. Give ONLY the step-by-step cooking instructions.
3. Give a Health Score from 0 to 100.
   - 80–100 = very healthy
   - 50–79 = moderately healthy
   - 0–49 = unhealthy/junk
4. Do NOT include explanations, tables, tips, or extra information.

Return output in this EXACT format:

Recipe Name: <name>

Steps:
1. ...
2. ...
3. ...

Health Score: <number>/100
"""

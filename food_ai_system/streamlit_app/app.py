import streamlit as st
import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from app.services.detection_service import detect_ingredients
from app.services.description_service import generate_description
from app.utils.storage import save_full_record
from app.agents.orchestrator import run_agent_pipeline
from app.services.edible_filter_service import filter_edible_items_ai



st.title("🍽 Multi-Image → Ingredient → Agentic AI Recipe System")

uploaded_files = st.file_uploader(
    "Upload one or more images of ingredients",
    type=["jpg", "png", "jpeg"],
    accept_multiple_files=True
)

if uploaded_files:

    all_detected_items = []
    all_ingredients = []

    os.makedirs("data", exist_ok=True)

    for uploaded_file in uploaded_files:

        image_path = os.path.join("data", uploaded_file.name)

        with open(image_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.image(image_path, caption=f"Uploaded: {uploaded_file.name}", use_column_width=True)

        raw_detected_items = detect_ingredients(image_path)
        
        print(raw_detected_items)

        detected_items = filter_edible_items_ai(raw_detected_items)


        st.subheader(f"🧠 Detected Ingredients in {uploaded_file.name}")
        for item in detected_items:
            st.write(f"- {item['name']} ({item['confidence']}%)")

        all_detected_items.extend(detected_items)

        for item in detected_items:
            all_ingredients.append(item["name"])

    unique_ingredients = list(set(all_ingredients))

    st.subheader("📦 Combined Ingredients")
    st.write(unique_ingredients)

    recipe_output = None
    research_summary = None

    if unique_ingredients:

        st.subheader("🤖 Agentic AI Generated Recipe")

        recipe_output, research_summary = run_agent_pipeline(unique_ingredients)

        st.subheader("🍽 Recipe")
        st.write(recipe_output)

    save_full_record(
        "multiple_images",
        all_detected_items,
        f"Combined ingredients from {len(uploaded_files)} images.",
        recipe_output,
        research_summary
    )

    print("\n===== TERMINAL OUTPUT =====")
    print("Combined Ingredients:", unique_ingredients)
    print("Recipe:", recipe_output)

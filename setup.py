import os

# Root folder
root = "food_ai_system"

# Folder structure
folders = [
    f"{root}/app/services",
    f"{root}/app/models",
    f"{root}/app/agents",
    f"{root}/app/utils",
    f"{root}/streamlit_app",
    f"{root}/data/test_images",
]

# Files to create
files = [
    f"{root}/app/main.py",
    f"{root}/app/services/detection_service.py",
    f"{root}/app/services/description_service.py",
    f"{root}/app/services/recipe_service.py",
    f"{root}/app/models/yolo_loader.py",
    f"{root}/app/agents/research_agent.py",
    f"{root}/app/agents/orchestrator.py",
    f"{root}/app/utils/image_utils.py",
    f"{root}/streamlit_app/app.py",
    f"{root}/requirements.txt",
    f"{root}/README.md",
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create empty files
for file in files:
    with open(file, "w") as f:
        pass

print("✅ Folder structure created successfully!")
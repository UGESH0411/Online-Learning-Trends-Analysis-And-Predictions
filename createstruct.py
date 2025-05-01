import os

# Define the project structure
project_structure = {
    "preprocessing": ["preprocess.py"],
    "eda": ["overview.py", "filtering.py", "insights.py", "visualization.py"],
    "ml": ["predict.py", "learning_curve.py"],
    "": ["app.py", "udemy_courses.csv"]  # Root files
}

# Create folders and files
for folder, files in project_structure.items():
    folder_path = os.path.join(os.getcwd(), folder)
    if folder and not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Created folder: {folder}")
    for file in files:
        file_path = os.path.join(folder_path, file) if folder else file
        with open(file_path, "w") as f:
            f.write("# " + file.split('.')[0].capitalize().replace("_", " ") + " module\n")
        print(f"Created file: {file_path}")

print("\n✅ Project structure created successfully!")

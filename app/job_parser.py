import os
from read_application import get_applications

df = get_applications()

skill_directory = [
    "python", "java", "javascript", "sql", "data structures",
    "algorithms", "object-oriented programming", "system design",
    "rest apis", "git", "cloud computing", "docker", "kubernetes",
    "ci/cd", "statistics", "machine learning", "deep learning",
    "data visualization", "pandas", "numpy", "scikit-learn",
    "tensorflow", "pytorch", "power bi", "tableau", "data cleaning",
    "data preprocessing", "feature engineering", "nlp",
    "computer vision", "generative ai", "llms", "transformers",
    "mlops", "model deployment"
]

filepath = "/Users/aady/Desktop/Ayush Vats/Projects/Job Application Tracker/Job Descriptions"

company_skillset = {}

for i in range(len(df)):
    id = df['id'].iloc[i]
    comp_name = df['company'].iloc[i]
    role = df['role'].iloc[i]

    role = str(role).replace(' ', '_') if role else "Unknown"

    path = os.path.join(filepath, f"{id}_{comp_name}_{role}.txt")

    skillset = []

    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            txt_file = f.read().lower()

        for skill in skill_directory:
            if skill in txt_file:
                skillset.append(skill)

    company_skillset[int(id)] = skillset

def extract_info():
    return company_skillset

import os
from read_application import get_applications

df = get_applications()
# print(df)

skill_directory = ["python", "java", "javascript", "sql", "data structures", "algorithms", "object-oriented programming", "system design", "rest apis", "git", "cloud computing", "docker", "kubernetes", "ci/cd", "statistics", "machine learning", "deep learning", "data visualization", "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch", "power bi", "tableau", "data cleaning", "data preprocessing", "feature engineering", "nlp", "computer vision", "generative ai", "llms", "transformers", "mlops", "model deployment"]

skill_dictionary = {
    'Software Role' : ["Data Structures & Algorithms", "Object-Oriented Programming", "Java", "Python", "JavaScript", "SQL", "REST APIs", "Git", "System Design", "Cloud Computing", "Docker", "Kubernetes", "CI/CD"],
    'Data Science' : ["Python", "SQL", "Statistics", "Machine Learning", "Data Visualization", "Pandas", "NumPy", "Scikit-learn", "Deep Learning", "TensorFlow", "PyTorch", "Power BI", "Tableau", "Data Cleaning", "Feature Engineering", "NLP"] ,
    'AI/ML': ["Python", "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch", "Scikit-learn", "NLP", "Computer Vision", "Generative AI", "LLMs", "Transformers", "MLOps", "Data Preprocessing", "Feature Engineering", "Model Deployment"],
}

# db.txt
filepath = "/Users/aady/Desktop/Ayush Vats/Projects/Job Application Tracker/Job Descriptions"
company_skillset = {}

for i in range(0,len(df)):
    id = df['id'].iloc[i]
    comp_name = df['company'].iloc[i]
    role = df['role'].iloc[i]

    if not role: role = 'Unknown'

    txt_file = ""
    path = os.path.join(filepath , f"{id}_{comp_name}_{role}.txt")
    if os.path.exists(path):
        with open(path, 'r') as f:
            txt_file = f.read()
            if(txt_file):
                arr = txt_file.split(' ')
                arr = [s.lower() for s in arr]

                skillset = []
                for itr in arr:
                    if(itr in skill_directory):
                        skillset.append(itr)

            company_skillset[int(id)] = skillset
            

print(company_skillset)


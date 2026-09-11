import os
from database_main import get_applications

df = get_applications()

skill_directory = ["Python", "Java", "JavaScript", "SQL", "Data Structures & Algorithms", "Object-Oriented Programming", "System Design", "REST APIs", "Git", "Cloud Computing", "Docker", "Kubernetes", "CI/CD", "Statistics", "Machine Learning", "Deep Learning", "Data Visualization", "Pandas", "NumPy", "Scikit-learn", "TensorFlow", "PyTorch", "Power BI", "Tableau", "Data Cleaning", "Data Preprocessing", "Feature Engineering", "NLP", "Computer Vision", "Generative AI", "LLMs", "Transformers", "MLOps", "Model Deployment"]

skill_dictionary = {
    'Software Role' : ["Data Structures & Algorithms", "Object-Oriented Programming", "Java", "Python", "JavaScript", "SQL", "REST APIs", "Git", "System Design", "Cloud Computing", "Docker", "Kubernetes", "CI/CD"],
    'Data Science' : ["Python", "SQL", "Statistics", "Machine Learning", "Data Visualization", "Pandas", "NumPy", "Scikit-learn", "Deep Learning", "TensorFlow", "PyTorch", "Power BI", "Tableau", "Data Cleaning", "Feature Engineering", "NLP"] ,
    'AI/ML': ["Python", "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch", "Scikit-learn", "NLP", "Computer Vision", "Generative AI", "LLMs", "Transformers", "MLOps", "Data Preprocessing", "Feature Engineering", "Model Deployment"],
}

# db.txt
filepath = "/Users/aady/Desktop/Ayush Vats/Projects/Job Application Tracker/Job Descriptions"
for i in range(0,len(df)):
    comp_name = df['company'].iloc[i]
    txt_file = ""
    path = os.path.join(filepath , f"")
    with open(path, 'r') as f:
        txt_file = f.read()
        print(txt_file)




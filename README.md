# Job Application Tracker & Automation System

A Python and Streamlit-based personal job application management and automation system that helps track applications, interviews, deadlines, follow-ups, job requirements, and application analytics in one centralized dashboard.

The system combines **database management, automation, analytics, job-description analysis, and optional AI assistance** to simplify the complete job application lifecycle.

---

## 🚀 Project Overview

Managing multiple job applications using spreadsheets, notes, and bookmarks quickly becomes difficult.

The **Job Application Tracker & Automation System** provides a centralized application for:

* Managing job applications
* Tracking application status
* Storing job descriptions
* Managing deadlines and follow-ups
* Tracking interviews
* Maintaining application activity history
* Extracting skills from job descriptions
* Comparing job requirements against resume skills
* Generating application analytics
* Exporting application data
* Optionally using an LLM for job-description analysis

The overall workflow is:

```text
Add Job
   ↓
Track Application
   ↓
Analyze Job Description
   ↓
Compare Resume Skills
   ↓
Set Deadline / Follow-up
   ↓
Receive Reminders
   ↓
Update Application Status
   ↓
Analyze Results
```

---

## 🎯 Problem Statement

Job seekers often manage applications using spreadsheets or scattered notes. This makes it difficult to:

* Keep track of application stages
* Remember deadlines
* Follow up on older applications
* Track interview rounds
* Understand which skills are frequently required
* Measure application and interview performance

This project addresses these problems through a single local application that combines **CRUD operations, automation, analytics, and job-description analysis**.

---

## ✨ Features

### 📋 Application Management

* Add new job applications
* Edit existing applications
* Delete applications
* Search applications
* Filter applications
* Store company and role information
* Store job URLs
* Track application dates
* Track deadlines
* Set application priority
* Add notes

### 🔄 Application Status Tracking

Applications can move through a standardized lifecycle:

```text
Saved
  ↓
Applied
  ↓
Assessment
  ↓
Interview
  ↓
Final Round
  ↓
Offer
```

Additional outcomes include:

* Rejected
* Withdrawn

---

### 🎤 Interview Tracking

Track multiple interviews associated with an application.

Supported information includes:

* Interview date
* Interview round
* Interview type
* Result
* Notes

Example interview types:

* Technical
* HR
* Managerial
* Final

---

### 📝 Activity History

Important application events can be recorded, such as:

```text
Application created
Status changed to Interview
Interview scheduled
Follow-up completed
```

Each activity is associated with the relevant application and timestamp.

---

### ⏰ Deadline Detection

The system automatically identifies upcoming and overdue deadlines.

Deadline classification:

| Days Remaining | Priority |
| -------------: | -------- |
|       > 7 days | Normal   |
|       3–7 days | Warning  |
|       ≤ 2 days | Urgent   |
|  Past deadline | Overdue  |

---

### 🔔 Follow-up Detection

The system can identify stale applications that may require follow-up.

Example rule:

```text
IF status = "Applied"
AND days since application > 7
AND no recent activity
THEN follow-up required
```

The dashboard can then display:

```text
FOLLOW-UP REQUIRED

Barclays
Decision Analyst
Applied 9 days ago
```

---

### 📊 Analytics Dashboard

Application statistics are calculated using Pandas.

The dashboard can display:

* Total applications
* Applications this week
* Applications this month
* Interviews
* Offers
* Rejections
* Interview rate
* Offer rate
* Applications over time
* Application status distribution
* Top companies applied to
* Pending actions

Example:

```text
Applications     37
Interviews        6
Offers            1
Pending Actions   5
```

---

### 🔎 Job Description Analysis

Users can store a complete job description and analyze it using rule-based text processing.

The system can:

1. Preprocess the job description
2. Search for known technical skills
3. Identify required skills
4. Compare those skills against configured resume skills

Example:

```text
Required Skills

✓ Python
✓ SQL
✓ SAS
✓ Statistics

✗ Docker
✗ AWS
```

The initial implementation uses **Python, regular expressions, and basic NLP/text processing** rather than complex NLP models.

---

### 🎯 Resume–Job Matching

The project provides a simple and transparent rule-based matching score.

For example:

```text
Required Skills:
Python
SQL
SAS
Statistics
Docker

Resume Skills:
Python
SQL
Docker

Matched Skills: 3
Required Skills: 5

Match Score: 60%
```

The score is intended as a **skill-overlap indicator**, not a probability of getting hired.

The dashboard also identifies:

**Matched**

* Python
* SQL
* Docker

**Missing**

* SAS
* Statistics

---

### 🤖 Optional AI Analysis

An optional OpenAI API integration can provide additional job-description analysis.

Potential capabilities include:

* Summarizing job descriptions
* Extracting important responsibilities
* Explaining required skills
* Suggesting resume areas to emphasize

API keys should be stored using environment variables and must never be committed to GitHub.

Example:

```text
OPENAI_API_KEY=your_api_key_here
```

AI functionality is intentionally added **after the core application is working**.

---

### 📤 Data Export

Application data can be exported as CSV files:

```text
applications.csv
interviews.csv
activities.csv
```

---

### 🐳 Docker Support

The application can optionally be containerized using Docker.

Example workflow:

```bash
docker build -t job-application-tracker .
docker run ...
```

Docker is treated as a packaging step rather than a prerequisite for development.

---

## 🏗️ System Architecture

The application follows a modular architecture:

```text
                   ┌──────────────────┐
                   │    Streamlit UI  │
                   └────────┬─────────┘
                            │
              ┌─────────────┴─────────────┐
              │                           │
              ▼                           ▼
    ┌──────────────────┐        ┌──────────────────┐
    │ Application      │        │ Job Analysis     │
    │ Module           │        │ Module           │
    └────────┬─────────┘        └────────┬─────────┘
             │                           │
             │                    ┌──────┴──────┐
             │                    │             │
             │                    ▼             ▼
             │              Skill Parser    AI API
             │
             └──────────────┬────────────────┘
                            ▼
                    ┌───────────────┐
                    │ SQLite        │
                    │ Database      │
                    └───────┬───────┘
                            │
              ┌─────────────┴─────────────┐
              ▼                           ▼
      ┌───────────────┐          ┌────────────────┐
      │ Reminder      │          │ Analytics      │
      │ Engine        │          │ Engine         │
      └───────┬───────┘          └───────┬────────┘
              │                           │
              ▼                           ▼
       Notifications                  Dashboard
```

The architecture is designed around a local SQLite database with Streamlit providing the user interface.

---

## 🛠️ Technology Stack

| Component            | Technology                            |
| -------------------- | ------------------------------------- |
| Programming Language | Python                                |
| Frontend / UI        | Streamlit                             |
| Database             | SQLite                                |
| Database Access      | Python `sqlite3` / SQL                |
| Data Analysis        | Pandas                                |
| Text Processing      | Python, Regex, Basic NLP              |
| AI                   | OpenAI API *(Optional)*               |
| Scheduling           | Python scheduling / cron              |
| Notifications        | Streamlit alerts / Email *(Optional)* |
| Web Extraction       | Requests + BeautifulSoup *(Optional)* |
| Testing              | pytest                                |
| Version Control      | Git + GitHub                          |
| Containerization     | Docker *(Optional)*                   |

---

## 🗄️ Database Design

The application uses three primary tables.

### Applications

```text
applications
--------------------------------
id
company
role
location
job_url
date_applied
deadline
status
priority
job_description
notes
created_at
updated_at
```

### Interviews

```text
interviews
--------------------------------
id
application_id
date
round
type
result
notes
```

### Activities

```text
activities
--------------------------------
id
application_id
activity
timestamp
notes
```

### Relationships

```text
APPLICATION
     │
     ├────────── INTERVIEWS
     │
     └────────── ACTIVITIES
```

One application can have multiple interviews and multiple activity records.

---

## 📁 Project Structure

The planned repository structure is:

```text
job-application-tracker/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── applications.py
│   ├── interviews.py
│   ├── activities.py
│   ├── reminders.py
│   ├── analytics.py
│   ├── job_parser.py
│   ├── resume_matcher.py
│   └── ai_analyzer.py
│
├── database/
│   └── schema.sql
│
├── data/
│   └── tracker.db
│
├── config/
│   ├── resume_skills.json
│   └── config.json
│
├── tests/
│   ├── test_database.py
│   ├── test_parser.py
│   ├── test_reminders.py
│   └── test_analytics.py
│
├── dashboard/
│   └── dashboard.py
│
├── .env
├── .gitignore
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd job-application-tracker
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on macOS/Linux:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

The OpenAI API key is only required if optional AI functionality is enabled.

**Never commit `.env` to GitHub.**

---

## ▶️ Running Locally

Start the Streamlit application:

```bash
streamlit run app/main.py
```

The application will open in your browser.

---

## 🐳 Running with Docker

Build the Docker image:

```bash
docker build -t job-application-tracker .
```

Run the container:

```bash
docker run -p 8501:8501 job-application-tracker
```

Then open:

```text
http://localhost:8501
```

Docker support is optional and is intended to be added after the core application is complete.

---

## 📊 Dashboard

The final dashboard is designed to provide a quick overview of the entire job search.

Example layout:

```text
=========================================================
             JOB APPLICATION TRACKER
=========================================================

Applications     Interviews     Offers     Actions
     37               6            1          5

---------------------------------------------------------
                    URGENT ACTIONS
---------------------------------------------------------

[!] Interview tomorrow - Company A
[!] Deadline in 2 days - Company B
[!] Follow-up required - Company C

---------------------------------------------------------
                 APPLICATION STATUS
---------------------------------------------------------

Applied       20
Assessment     7
Interview      5
Rejected       6
Offer          1

---------------------------------------------------------
                RECENT APPLICATIONS
---------------------------------------------------------

Company       Role                Status
---------------------------------------------------------
Barclays      Decision Analyst    Interview
Google        Data Analyst        Applied
Microsoft     SDE                 Assessment

---------------------------------------------------------
                    JOB ANALYSIS
---------------------------------------------------------

Selected Job: Decision Analyst
Match Score: 78%

Matched:
✓ Python
✓ SQL
✓ Statistics

Missing:
⚠ SAS
⚠ Forecasting
```

---

## 🔄 End-to-End Workflow

A typical workflow looks like:

### 1. Add a Job

Enter:

```text
Company: Barclays
Role: Decision Analyst
Status: Applied
Priority: High
```

### 2. Add Job Description

Paste the complete job description into the application.

### 3. Analyze the Job

The system extracts relevant skills such as:

```text
Python
SQL
SAS
Statistics
Forecasting
Data Analytics
```

### 4. Compare Resume

The extracted skills are compared with the configured resume skills.

```text
Match Score: 75%

Matched:
✓ Python
✓ SQL
✓ Statistics

Missing:
⚠ SAS
⚠ Forecasting
```

### 5. Track the Application

The application is saved in SQLite and displayed on the dashboard.

### 6. Set Follow-up

The system tracks the follow-up date.

### 7. Detect Stale Applications

If an application has had no activity for an extended period, the system flags it for follow-up.

### 8. Track Interviews

Move the application through:

```text
Applied
   ↓
Assessment
   ↓
Interview
```

and record interview details.

### 9. Analyze Results

The dashboard displays application and interview statistics.

### 10. Export Data

Download application data as CSV.

---

## 🧪 Testing

The project uses `pytest` for automated testing.

Test modules include:

```text
tests/
├── test_database.py
├── test_parser.py
├── test_reminders.py
└── test_analytics.py
```

Important functionality to test:

* Adding an application
* Updating application status
* Deleting an application
* Skill extraction
* Match-score calculation
* Deadline detection
* Follow-up detection

Run tests with:

```bash
pytest
```

---

## 🔐 Security

If AI functionality is enabled:

* Store API keys in environment variables
* Never hard-code API keys
* Never commit `.env`
* Add `.env` to `.gitignore`

Example:

```text
.env
__pycache__/
*.pyc
venv/
data/*.db
```

---

## 🔮 Optional Features

The following features can be added after the core application is complete.

### Web Job Description Extraction

Users can provide a job URL and the application can optionally attempt:

```text
URL
 ↓
Requests
 ↓
HTML
 ↓
BeautifulSoup
 ↓
Job Description
```

This remains optional because job websites can have significantly different page structures.

### Email Notifications

The system can optionally send reminders such as:

```text
Job Tracker Reminder

You have 3 actions today:

1. Follow up with Barclays
2. Interview with Company B
3. Application deadline for Company C
```

### AI Resume Suggestions

Given a resume and job description, AI can suggest:

* Skills to emphasize
* Potential missing skills
* Areas of the resume to improve

### Weekly Report

A weekly job-search report can summarize:

```text
WEEKLY JOB SEARCH REPORT

Applications: 8
Interviews: 2
Rejections: 1
Offers: 0

Top applied role: Data Analyst
Most common required skill: SQL
Pending actions: 4
```

---

## 🚫 What This Project Does NOT Build

To keep the project focused and achievable, the following are intentionally excluded:

* Automatic LinkedIn applications
* Automatic application submission
* Browser automation across dozens of job websites
* Complex React frontend
* PostgreSQL deployment
* Microservices
* Complex NLP models
* Training an LLM
* Complex authentication
* Cloud deployment

These features would significantly increase development complexity and development time.

---

## 📈 Future Improvements

Potential future improvements include:

* Email notification integration
* Improved job-description extraction
* More advanced skill matching
* Additional analytics
* Weekly automated reports
* More sophisticated NLP-based job analysis
* Additional export formats
* Deployment to a cloud platform

---

## 🎓 Learning Outcomes

This project provides practical experience with:

* Python
* SQL
* SQLite
* CRUD application development
* Streamlit
* Pandas
* Data visualization
* Text processing
* APIs
* LLM integration
* Scheduling
* Automation
* Git/GitHub
* Docker
* Testing
* Application architecture

More importantly, the project demonstrates how to combine:

```text
Database
    +
Automation
    +
Analytics
    +
AI
    +
User Interface
```

into a single end-to-end application.

---

## 📌 Development Philosophy

The project follows this development order:

```text
SQLite
  ↓
CRUD
  ↓
Streamlit
  ↓
Automation
  ↓
Analytics
  ↓
Job Analysis
  ↓
AI
  ↓
Docker
```

The core workflow should be made reliable before adding AI, web scraping, or containerization.

---

## 💼 Resume Description

A concise resume description for the completed project:

> **Job Application Tracker & Automation System** — Developed a Python and Streamlit-based job application management system using SQLite and Pandas to track applications, interviews, deadlines, and follow-ups. Automated deadline and stale-application detection and implemented job-description skill extraction and resume-job matching. Integrated an optional LLM-based analysis module for job summarization and skill recommendations and containerized the application using Docker.

---

## 👨‍💻 Author

**Your Name**

GitHub: `<YOUR_GITHUB_PROFILE>`

LinkedIn: `<YOUR_LINKEDIN_PROFILE>`

---

## ⭐ Project Status

**Status:** In Development

**Planned Duration:** 5 Weeks

**Estimated Effort:** 40–50 Hours

**Primary Language:** Python

**Interface:** Streamlit

**Database:** SQLite

**Analytics:** Pandas

**AI:** OpenAI API

**Containerization:** Docker


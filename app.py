from flask import Flask, render_template, request, redirect, url_for
import pdfplumber
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# ---------- SKILLS ----------
skills_list = [
    "python",
    "java",
    "html",
    "css",
    "javascript",
    "flask",
    "sql",
    "react",
    "machine learning"
]

# ---------- CAREER PATH ----------
career_roles = {
    "python": ["Backend Developer", "AI Engineer"],
    "java": ["Java Developer"],
    "html": ["Frontend Developer"],
    "css": ["UI Developer"],
    "javascript": ["Full Stack Developer"],
    "flask": ["Python Web Developer"],
    "sql": ["Database Developer"],
    "react": ["Frontend Engineer"],
    "machine learning": ["ML Engineer", "Data Scientist"]
}

# ---------- CERTIFICATIONS ----------
certifications = {
    "python": [
        "Google Python Certificate",
        "Python for Everybody"
    ],

    "java": [
        "Oracle Java Certification"
    ],

    "html": [
        "HTML5 Certification"
    ],

    "css": [
        "CSS Mastery Course"
    ],

    "javascript": [
        "JavaScript Advanced"
    ],

    "flask": [
        "Flask Web Development"
    ],

    "sql": [
        "SQL Certification"
    ],

    "react": [
        "React Developer Course"
    ],

    "machine learning": [
        "Andrew Ng ML Course"
    ]
}

# ---------- INTERNSHIPS ----------
internships = {
    "python": [
        "Python Intern at Infosys"
    ],

    "java": [
        "Java Intern at TCS"
    ],

    "html": [
        "Frontend Intern"
    ],

    "css": [
        "UI Design Intern"
    ],

    "javascript": [
        "Frontend Developer Intern"
    ],

    "flask": [
        "Backend Flask Intern"
    ],

    "sql": [
        "Database Intern"
    ],

    "react": [
        "React Intern"
    ],

    "machine learning": [
        "AI/ML Intern"
    ]
}

# GLOBAL STORAGE
detected_skills = []
ats_score = 0

# ---------- HOME ----------
@app.route("/", methods=["GET", "POST"])
def index():

    global detected_skills
    global ats_score

    if request.method == "POST":

        file = request.files["resume"]

        if file:

            filepath = os.path.join(
                app.config["UPLOAD_FOLDER"],
                file.filename
            )

            file.save(filepath)

            text = ""

            with pdfplumber.open(filepath) as pdf:

                for page in pdf.pages:

                    extracted = page.extract_text()

                    if extracted:
                        text += extracted.lower()

            detected_skills = []

            for skill in skills_list:

                if skill.lower() in text:
                    detected_skills.append(skill)

            # ATS SCORE
            ats_score = min(len(detected_skills) * 10, 100)

            return redirect(url_for("result"))

    return render_template("index.html")

# ---------- RESULT ----------
@app.route("/result")
def result():

    return render_template(
        "result.html",
        skills=detected_skills,
        score=ats_score,
        certifications=certifications,
        internships=internships
    )

# ---------- CAREER PAGE ----------
@app.route("/career/<skill>")
def career(skill):

    roadmap_data = {

        "python": {

            "description":
            "Python is used in AI, backend development, automation and data science.",

            "roadmap": [

                "Learn Python Basics",
                "Practice Loops and Functions",
                "Learn OOP in Python",
                "Build Mini Projects",
                "Learn Flask/Django",
                "Learn Database (SQL)",
                "Build Full Stack Projects",
                "Learn APIs and Deployment",
                "Apply for Internships",
                "Become Backend Developer / AI Engineer"
            ],

            "roles": [

                "Backend Developer",
                "AI Engineer",
                "Automation Engineer",
                "Data Analyst"
            ],

            "companies": [

                "TCS",
                "Infosys",
                "Wipro",
                "Accenture",
                "Cognizant",
                "Google",
                "Microsoft",
                "Amazon"
            ]
        },

        "java": {

            "description":
            "Java is used in enterprise applications and Android apps.",

            "roadmap": [

                "Learn Java Basics",
                "Practice OOP Concepts",
                "Learn JDBC",
                "Learn Spring Boot",
                "Build REST APIs",
                "Build Projects",
                "Learn MySQL",
                "Apply for Java Internships",
                "Become Java Developer"
            ],

            "roles": [

                "Java Developer",
                "Backend Developer",
                "Android Developer"
            ],

            "companies": [

                "TCS",
                "Infosys",
                "Oracle",
                "IBM",
                "Capgemini",
                "Accenture"
            ]
        },

        "sql": {

            "description":
            "SQL is used for database management and analytics.",

            "roadmap": [

                "Learn SQL Basics",
                "Practice Queries",
                "Learn Joins",
                "Learn Database Design",
                "Learn MySQL/PostgreSQL",
                "Work on Data Projects",
                "Become Data Analyst"
            ],

            "roles": [

                "Database Administrator",
                "Data Analyst",
                "SQL Developer"
            ],

            "companies": [

                "Oracle",
                "Infosys",
                "Wipro",
                "IBM",
                "TCS"
            ]
        }
    }

    data = roadmap_data.get(skill.lower())

    return render_template(
        "career_detail.html",
        skill=skill,
        data=data
    )
if __name__ == "__main__":
    app.run(debug=True)
import os
import re
from flask import Flask, render_template, request

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

app = Flask(
    __name__,
    template_folder=TEMPLATE_DIR
)

SKILLS = [
    "python",
    "java",
    "c++",
    "sql",
    "html",
    "css",
    "javascript",
    "machine learning",
    "deep learning",
    "data analysis",
    "data science",
    "excel",
    "pandas",
    "numpy",
    "flask",
    "django",
    "communication",
    "problem solving",
    "power bi",
    "tensorflow",
    "scikit-learn"
]


def extract_skills(text):
    text = text.lower()
    found = []

    for skill in SKILLS:
        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

        if re.search(pattern, text):
            found.append(skill)

    return found


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        resume = request.form.get("resume", "").strip()
        job_description = request.form.get(
            "job_description", ""
        ).strip()

        if not resume or not job_description:
            result = {
                "error": "Please enter both resume and job description."
            }

        else:
            resume_skills = extract_skills(resume)
            job_skills = extract_skills(job_description)

            matched = [
                skill for skill in job_skills
                if skill in resume_skills
            ]

            missing = [
                skill for skill in job_skills
                if skill not in resume_skills
            ]

            if job_skills:
                percentage = round(
                    len(matched) / len(job_skills) * 100
                )
            else:
                percentage = 0

            if percentage >= 70:
                summary = "Good potential match for this role."
            elif percentage >= 40:
                summary = (
                    "Partial match. Some skills need improvement."
                )
            else:
                summary = (
                    "Low keyword match. More relevant skills may be needed."
                )

            result = {
                "matched": matched,
                "missing": missing,
                "percentage": percentage,
                "summary": summary
            }

    return render_template(
        "index.html",
        result=result
    )


if __name__ == "__main__":
    print("Project folder:", BASE_DIR)
    print("Templates folder:", TEMPLATE_DIR)
    print(
        "HTML file exists:",
        os.path.isfile(
            os.path.join(TEMPLATE_DIR, "index.html")
        )
    )

    app.run(debug=True)
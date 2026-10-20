AI-Based Resume Screening System

Project Overview

The AI-Based Resume Screening System is a Python-based web application that compares a candidate's resume with a job description. It identifies matching skills, missing skills, and calculates a keyword match percentage.

Objectives

- Automate basic resume screening.
- Identify skills matching the job requirements.
- Highlight missing skills.
- Display a resume match percentage.
- Provide a simple and user-friendly interface.

Technologies Used

- Python
- Flask
- HTML
- CSS
- Regular Expressions
- Visual Studio Code

Features

- Resume text input.
- Job description input.
- Automatic skill extraction.
- Matching and missing skill identification.
- Resume match percentage calculation.
- Match summary.

Project Structure

- "app.py" — Main Python application.
- "templates/index.html" — User interface.
- "screenshots/" — Project testing screenshots.
- "README.md" — Project documentation.

How to Run

1. Install Python.
2. Install Flask using "pip install flask".
3. Open the project folder in Visual Studio Code.
4. Run "python app.py" in the terminal.
5. Open the local URL displayed in the terminal in a browser.
6. Enter the resume and job description, then click Analyze Resume.

Testing

The application was tested using sample resume text and job descriptions.

- Test 1: Partial skill match — 71% match.
- Test 2: All seven required skills matched — 100% match.

Screenshots of the test results are available in the "screenshots" folder.

Limitations

The current system uses keyword matching rather than a trained AI model. Results depend on the skills listed in the application and may not fully represent a candidate's qualifications.

Future Enhancements

- Support PDF and DOCX resume uploads.
- Use Natural Language Processing (NLP).
- Add more skills and job categories.
- Improve matching accuracy.
- Store screening results in a database.

Conclusion

The AI-Based Resume Screening System demonstrates how Python and Flask can be used to compare resume skills with job requirements through a simple web interface. It helps identify matching and missing skills and provides a basic match percentage.
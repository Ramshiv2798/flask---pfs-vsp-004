import uuid
from flask import Flask, render_template

app = Flask(__name__)

# Static routes: '/' and '/home' render resume.html
@app.route("/")
@app.route("/home")
def home():
    return render_template("resume.html")

# Navigation target: about page
@app.route("/about")
def about():
    return render_template("about.html")

# Dynamic route: subject name and marks (accepts int or float)
# Example: /subject/Maths/87 or /subject/Maths/87.5
@app.route("/subject/<string:subject>/<marks>")
def subject_marks(subject, marks):
    try:
        marks_val = float(marks)
    except ValueError:
        return "Marks must be a number"
    return f"Subject: {subject}, Marks: {marks_val}"

# Dynamic route: generate a UUID for a subject
# Example: /uuid/Physics
@app.route("/uuid/<string:subject>")
def subject_uuid(subject):
    return f"Subject: {subject}, UUID: {uuid.uuid4()}"

if __name__ == "__main__":
    app.run(debug=True)

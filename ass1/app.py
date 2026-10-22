from flask import Flask, render_template,url_for,redirect
import uuid

app = Flask(__name__)

@app.route("/")
def welcome():
    return redirect(url_for('index'))

@app.route("/index")
def index():
    return render_template("resume.html")

@app.route("/home")
def home():
    return render_template("resume.html")

@app.route("/subject/<subject>/<float:marks>")
def subject(subject, marks):
    return f"""
    <h1>Subject Details</h1>
    <p>Subject: {subject}</p>
    <p>Marks: {marks}</p>
    """
    
@app.route("/uuid/<subject>")
def subject_uuid(subject):
    generated_uuid = uuid.uuid4()
    return f"""
    <h1>Subject UUID</h1>
    <p>Subject: {subject}</p>
    <p>UUID: {generated_uuid}</p>
    """
    
@app.route("/about")
def about():
    return """
    <center>
    <h1>About Page</h1>
    <p>This is my resume Flask application.</p>
    <a href="/">Back to Home</a>
    </center>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5100,debug=True)
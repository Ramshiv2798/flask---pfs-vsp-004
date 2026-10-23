from flask import Flask, render_template

app = Flask(__name__)

students = [
    {"id": 1, "name": "Ram", "percentage": 92},
    {"id": 2, "name": "Krishna", "percentage": 84},
    {"id": 3, "name": "Sai", "percentage": 78},
    {"id": 4, "name": "Ravi", "percentage": 67},
    {"id": 5, "name": "Priya", "percentage": 88},
    {"id": 6, "name": "Anu", "percentage": 73},
    {"id": 7, "name": "Kiran", "percentage": 59},
    {"id": 8, "name": "Deepika", "percentage": 81},
    {"id": 9, "name": "Manoj", "percentage": 46},
    {"id": 10, "name": "Sneha", "percentage": 95}
]

def calculate_grade(percentage):
    if percentage > 80:
        return "A"
    elif percentage > 70:
        return "B"
    elif percentage > 60:
        return "C"
    elif percentage > 50:
        return "D"
    else:
        return "F"

@app.route('/')
def home():
    for student in students:
        student["grade"] = calculate_grade(student["percentage"])
    return render_template('students.html', students=students)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
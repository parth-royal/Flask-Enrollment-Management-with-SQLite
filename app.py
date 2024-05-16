from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# ORM Models
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    enrollment_date = db.Column(db.Date, nullable=False)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enrollments', methods=['POST'])
def add_enrollment():
    student_id = request.form['StudentId']
    course_id = request.form['CourseId']
    enrollment_date_str = request.form['EnrollmentDate']
    enrollment_date = datetime.strptime(enrollment_date_str, '%Y-%m-%d').date()

    enrollment = Enrollment(student_id=student_id, course_id=course_id, enrollment_date=enrollment_date)
    db.session.add(enrollment)
    db.session.commit()
    return 'Enrollment added successfully'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

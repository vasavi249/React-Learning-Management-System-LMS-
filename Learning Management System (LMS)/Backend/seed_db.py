import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Backend.settings')
django.setup()

from lms.models import Student, Instructor, Course, Enrollment, Assignment
from datetime import datetime

def seed():
    print("Clearing database...")
    Student.objects.all().delete()
    Instructor.objects.all().delete()
    Course.objects.all().delete()
    Enrollment.objects.all().delete()
    Assignment.objects.all().delete()

    print("Adding Students...")
    student1 = Student.objects.create(
        student_id=101,
        full_name="Rahul Sharma",
        email="rahul@gmail.com",
        phone="9876543210",
        qualification="B.Tech",
        password="rahul123"
    )

    print("Adding Instructors...")
    inst1 = Instructor.objects.create(
        instructor_id=201,
        instructor_name="Saran Velmurugan",
        specialization="Full Stack Development",
        experience=5,
        email="trainer@gmail.com",
        phone="9876543211"
    )
    inst2 = Instructor.objects.create(
        instructor_id=202,
        instructor_name="Kumar",
        specialization="Java Full Stack Development",
        experience=7,
        email="kumar@gmail.com",
        phone="9876543212"
    )
    inst3 = Instructor.objects.create(
        instructor_id=203,
        instructor_name="Priya",
        specialization="Data Science & AI",
        experience=6,
        email="priya@gmail.com",
        phone="9876543213"
    )

    print("Adding Courses...")
    course1 = Course.objects.create(
        course_id=301,
        course_name="Python Full Stack",
        instructor_name="Saran Velmurugan",
        category="Programming",
        duration="6 Months",
        price=25000.0,
        level="Beginner"
    )
    course2 = Course.objects.create(
        course_id=302,
        course_name="Java Full Stack",
        instructor_name="Kumar",
        category="Programming",
        duration="5 Months",
        price=22000.0,
        level="Intermediate"
    )
    course3 = Course.objects.create(
        course_id=303,
        course_name="Data Science",
        instructor_name="Priya",
        category="AI & ML",
        duration="8 Months",
        price=30000.0,
        level="Advanced"
    )
    course4 = Course.objects.create(
        course_id=304,
        course_name="Django Development",
        instructor_name="Saran Velmurugan",
        category="Backend",
        duration="4 Months",
        price=18000.0,
        level="Beginner"
    )
    course5 = Course.objects.create(
        course_id=305,
        course_name="React Frontend Development",
        instructor_name="Saran Velmurugan",
        category="Frontend",
        duration="3 Months",
        price=15000.0,
        level="Intermediate"
    )
    course6 = Course.objects.create(
        course_id=306,
        course_name="Machine Learning Specialization",
        instructor_name="Priya",
        category="AI & ML",
        duration="6 Months",
        price=28000.0,
        level="Advanced"
    )
    course7 = Course.objects.create(
        course_id=307,
        course_name="NodeJS Microservices",
        instructor_name="Kumar",
        category="Backend",
        duration="4 Months",
        price=17000.0,
        level="Advanced"
    )
    course8 = Course.objects.create(
        course_id=308,
        course_name="Introduction to Web Development",
        instructor_name="Kumar",
        category="Programming",
        duration="2 Months",
        price=10000.0,
        level="Beginner"
    )
    course9 = Course.objects.create(
        course_id=309,
        course_name="VueJS Single Page Apps",
        instructor_name="Saran Velmurugan",
        category="Frontend",
        duration="3 Months",
        price=14000.0,
        level="Beginner"
    )
    course10 = Course.objects.create(
        course_id=310,
        course_name="Deep Learning & Neural Networks",
        instructor_name="Priya",
        category="AI & ML",
        duration="7 Months",
        price=32000.0,
        level="Advanced"
    )
    course11 = Course.objects.create(
        course_id=311,
        course_name="Tailwind CSS Essentials",
        instructor_name="Saran Velmurugan",
        category="Frontend",
        duration="1 Month",
        price=5000.0,
        level="Beginner"
    )
    course12 = Course.objects.create(
        course_id=312,
        course_name="Natural Language Processing (NLP)",
        instructor_name="Priya",
        category="AI & ML",
        duration="5 Months",
        price=27000.0,
        level="Intermediate"
    )
    course13 = Course.objects.create(
        course_id=313,
        course_name="Flutter Mobile App Development",
        instructor_name="Kumar",
        category="Mobile Development",
        duration="4 Months",
        price=16000.0,
        level="Intermediate"
    )
    course14 = Course.objects.create(
        course_id=314,
        course_name="Cybersecurity Essentials",
        instructor_name="Priya",
        category="Security",
        duration="3 Months",
        price=12000.0,
        level="Beginner"
    )
    course15 = Course.objects.create(
        course_id=315,
        course_name="SQL & Relational Databases",
        instructor_name="Kumar",
        category="Database",
        duration="2 Months",
        price=8000.0,
        level="Beginner"
    )
    course16 = Course.objects.create(
        course_id=316,
        course_name="DevOps & AWS Cloud",
        instructor_name="Saran Velmurugan",
        category="Cloud Computing",
        duration="5 Months",
        price=24000.0,
        level="Advanced"
    )

    print("Adding Enrollments...")
    enroll1 = Enrollment.objects.create(
        enrollment_id=401,
        student_name="Rahul Sharma",
        course_name="Python Full Stack",
        enrollment_date=datetime.strptime("2026-07-15", "%Y-%m-%d").date(),
        payment_status="Paid",
        course_status="Active"
    )
    enroll2 = Enrollment.objects.create(
        enrollment_id=402,
        student_name="Rahul Sharma",
        course_name="Java Full Stack",
        enrollment_date=datetime.strptime("2026-07-15", "%Y-%m-%d").date(),
        payment_status="Pending",
        course_status="Active"
    )
    enroll3 = Enrollment.objects.create(
        enrollment_id=403,
        student_name="Rahul Sharma",
        course_name="Data Science",
        enrollment_date=datetime.strptime("2026-07-10", "%Y-%m-%d").date(),
        payment_status="Paid",
        course_status="Completed"
    )
    enroll4 = Enrollment.objects.create(
        enrollment_id=404,
        student_name="Rahul Sharma",
        course_name="Django Development",
        enrollment_date=datetime.strptime("2026-07-12", "%Y-%m-%d").date(),
        payment_status="Paid",
        course_status="Active"
    )
    enroll5 = Enrollment.objects.create(
        enrollment_id=405,
        student_name="Rahul Sharma",
        course_name="React Frontend Development",
        enrollment_date=datetime.strptime("2026-07-14", "%Y-%m-%d").date(),
        payment_status="Paid",
        course_status="Active"
    )

    print("Adding Assignments...")
    Assignment.objects.create(
        assignment_id=501,
        course_name="Python Full Stack",
        student_name="Rahul Sharma",
        assignment_title="Student Management System",
        submission_date=datetime.strptime("2026-07-25", "%Y-%m-%d").date(),
        marks=95,
        status="Evaluated"
    )
    Assignment.objects.create(
        assignment_id=502,
        course_name="Python Full Stack",
        student_name="Rahul Sharma",
        assignment_title="Django REST APIs Blog API",
        submission_date=None,
        marks=None,
        status="Pending"
    )
    Assignment.objects.create(
        assignment_id=503,
        course_name="Java Full Stack",
        student_name="Rahul Sharma",
        assignment_title="Library Management System",
        submission_date=None,
        marks=None,
        status="Pending"
    )
    Assignment.objects.create(
        assignment_id=504,
        course_name="Java Full Stack",
        student_name="Rahul Sharma",
        assignment_title="Spring Boot MVC Shopping Cart",
        submission_date=datetime.strptime("2026-07-26", "%Y-%m-%d").date(),
        marks=88,
        status="Evaluated"
    )
    Assignment.objects.create(
        assignment_id=505,
        course_name="Data Science",
        student_name="Rahul Sharma",
        assignment_title="Pandas Data Analytics Report",
        submission_date=datetime.strptime("2026-07-20", "%Y-%m-%d").date(),
        marks=90,
        status="Evaluated"
    )
    Assignment.objects.create(
        assignment_id=506,
        course_name="Data Science",
        student_name="Rahul Sharma",
        assignment_title="Customer Churn Prediction Model",
        submission_date=datetime.strptime("2026-07-28", "%Y-%m-%d").date(),
        marks=94,
        status="Evaluated"
    )
    Assignment.objects.create(
        assignment_id=507,
        course_name="Django Development",
        student_name="Rahul Sharma",
        assignment_title="E-learning Platform Database Design",
        submission_date=None,
        marks=None,
        status="Pending"
    )
    Assignment.objects.create(
        assignment_id=508,
        course_name="React Frontend Development",
        student_name="Rahul Sharma",
        assignment_title="Single Page Application Dashboard",
        submission_date=None,
        marks=None,
        status="Pending"
    )
    Assignment.objects.create(
        assignment_id=509,
        course_name="React Frontend Development",
        student_name="Rahul Sharma",
        assignment_title="React Router & Hooks Practice",
        submission_date=None,
        marks=None,
        status="Pending"
    )
    Assignment.objects.create(
        assignment_id=510,
        course_name="Django Development",
        student_name="Rahul Sharma",
        assignment_title="Django Forms & Custom Validation",
        submission_date=None,
        marks=None,
        status="Pending"
    )
    Assignment.objects.create(
        assignment_id=511,
        course_name="Python Full Stack",
        student_name="Rahul Sharma",
        assignment_title="Algorithm Complexity and Data Structures",
        submission_date=None,
        marks=None,
        status="Pending"
    )
    Assignment.objects.create(
        assignment_id=512,
        course_name="Java Full Stack",
        student_name="Rahul Sharma",
        assignment_title="Multithreading & Concurrency",
        submission_date=None,
        marks=None,
        status="Pending"
    )

    print("Database seeded successfully!")

if __name__ == "__main__":
    seed()

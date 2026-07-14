from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student, Instructor, Course, Enrollment, Assignment
import json

# Utility Helper to retrieve objects by primary key 'id' OR logical identifier field
def get_object_by_id_or_field(model, identifier, field_name):
    # Try looking up by database internal primary key 'id' (integer)
    try:
        val = int(identifier)
        return model.objects.get(id=val)
    except (model.DoesNotExist, ValueError):
        pass

    # Try looking up by logical ID field (e.g. student_id, course_id, etc.)
    try:
        val = int(identifier)
        kwargs = {field_name: val}
        return model.objects.get(**kwargs)
    except (model.DoesNotExist, ValueError):
        return None

# ==================== STUDENT VIEWS ====================

# GET /students/
def students(request):
    if request.method == "GET":
        data = list(Student.objects.values())
        return JsonResponse(data, safe=False)
    return JsonResponse({"error": "Method Not Allowed"}, status=405)

# POST /students/add/
@csrf_exempt
def add_student(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            student = Student.objects.create(
                student_id=int(body["student_id"]),
                full_name=body["full_name"],
                email=body["email"],
                phone=body["phone"],
                qualification=body["qualification"],
                password=body["password"]
            )
            return JsonResponse({"message": "Student Added Successfully", "id": student.id})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method Not Allowed"}, status=405)

# PUT /students/update/<id>/
@csrf_exempt
def update_student(request, id):
    if request.method == "PUT":
        try:
            student = get_object_by_id_or_field(Student, id, "student_id")
            if not student:
                return JsonResponse({"error": "Student not found"}, status=404)
            
            body = json.loads(request.body)
            student.student_id = int(body.get("student_id", student.student_id))
            student.full_name = body.get("full_name", student.full_name)
            student.email = body.get("email", student.email)
            student.phone = body.get("phone", student.phone)
            student.qualification = body.get("qualification", student.qualification)
            student.password = body.get("password", student.password)
            student.save()
            return JsonResponse({"message": "Student Updated Successfully"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method Not Allowed"}, status=405)

# DELETE /students/delete/<id>/
@csrf_exempt
def delete_student(request, id):
    if request.method == "DELETE":
        student = get_object_by_id_or_field(Student, id, "student_id")
        if not student:
            return JsonResponse({"error": "Student not found"}, status=404)
        student.delete()
        return JsonResponse({"message": "Student Deleted Successfully"})
    return JsonResponse({"error": "Method Not Allowed"}, status=405)


# ==================== INSTRUCTOR VIEWS ====================

# GET /instructors/
def instructors(request):
    if request.method == "GET":
        data = list(Instructor.objects.values())
        return JsonResponse(data, safe=False)
    return JsonResponse({"error": "Method Not Allowed"}, status=405)

# POST /instructors/add/
@csrf_exempt
def add_instructor(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            instructor = Instructor.objects.create(
                instructor_id=int(body["instructor_id"]),
                instructor_name=body["instructor_name"],
                specialization=body["specialization"],
                experience=int(body["experience"]),
                email=body["email"],
                phone=body["phone"]
            )
            return JsonResponse({"message": "Instructor Added Successfully", "id": instructor.id})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method Not Allowed"}, status=405)

# PUT /instructors/update/<id>/
@csrf_exempt
def update_instructor(request, id):
    if request.method == "PUT":
        try:
            instructor = get_object_by_id_or_field(Instructor, id, "instructor_id")
            if not instructor:
                return JsonResponse({"error": "Instructor not found"}, status=404)
            
            body = json.loads(request.body)
            instructor.instructor_id = int(body.get("instructor_id", instructor.instructor_id))
            instructor.instructor_name = body.get("instructor_name", instructor.instructor_name)
            instructor.specialization = body.get("specialization", instructor.specialization)
            instructor.experience = int(body.get("experience", instructor.experience))
            instructor.email = body.get("email", instructor.email)
            instructor.phone = body.get("phone", instructor.phone)
            instructor.save()
            return JsonResponse({"message": "Instructor Updated Successfully"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method Not Allowed"}, status=405)

# DELETE /instructors/delete/<id>/
@csrf_exempt
def delete_instructor(request, id):
    if request.method == "DELETE":
        instructor = get_object_by_id_or_field(Instructor, id, "instructor_id")
        if not instructor:
            return JsonResponse({"error": "Instructor not found"}, status=404)
        instructor.delete()
        return JsonResponse({"message": "Instructor Deleted Successfully"})
    return JsonResponse({"error": "Method Not Allowed"}, status=405)


# ==================== COURSE VIEWS ====================

# GET /courses/
def courses(request):
    if request.method == "GET":
        data = list(Course.objects.values())
        return JsonResponse(data, safe=False)
    return JsonResponse({"error": "Method Not Allowed"}, status=405)

# POST /courses/add/
@csrf_exempt
def add_course(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            course = Course.objects.create(
                course_id=int(body["course_id"]),
                course_name=body["course_name"],
                instructor_name=body["instructor_name"],
                category=body["category"],
                duration=body["duration"],
                price=float(body["price"]),
                level=body["level"]
            )
            return JsonResponse({"message": "Course Added Successfully", "id": course.id})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method Not Allowed"}, status=405)

# PUT /courses/update/<id>/
@csrf_exempt
def update_course(request, id):
    if request.method == "PUT":
        try:
            course = get_object_by_id_or_field(Course, id, "course_id")
            if not course:
                return JsonResponse({"error": "Course not found"}, status=404)
            
            body = json.loads(request.body)
            course.course_id = int(body.get("course_id", course.course_id))
            course.course_name = body.get("course_name", course.course_name)
            course.instructor_name = body.get("instructor_name", course.instructor_name)
            course.category = body.get("category", course.category)
            course.duration = body.get("duration", course.duration)
            course.price = float(body.get("price", course.price))
            course.level = body.get("level", course.level)
            course.save()
            return JsonResponse({"message": "Course Updated Successfully"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method Not Allowed"}, status=405)

# DELETE /courses/delete/<id>/
@csrf_exempt
def delete_course(request, id):
    if request.method == "DELETE":
        course = get_object_by_id_or_field(Course, id, "course_id")
        if not course:
            return JsonResponse({"error": "Course not found"}, status=404)
        course.delete()
        return JsonResponse({"message": "Course Deleted Successfully"})
    return JsonResponse({"error": "Method Not Allowed"}, status=405)


# ==================== ENROLLMENT VIEWS ====================

# GET /enrollments/
def enrollments(request):
    if request.method == "GET":
        data = list(Enrollment.objects.values())
        return JsonResponse(data, safe=False)
    return JsonResponse({"error": "Method Not Allowed"}, status=405)

# POST /enrollments/add/
@csrf_exempt
def add_enrollment(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            enrollment = Enrollment.objects.create(
                enrollment_id=int(body["enrollment_id"]),
                student_name=body["student_name"],
                course_name=body["course_name"],
                enrollment_date=body["enrollment_date"],
                payment_status=body["payment_status"],
                course_status=body["course_status"]
            )
            return JsonResponse({"message": "Enrollment Added Successfully", "id": enrollment.id})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method Not Allowed"}, status=405)

# PUT /enrollments/update/<id>/
@csrf_exempt
def update_enrollment(request, id):
    if request.method == "PUT":
        try:
            enrollment = get_object_by_id_or_field(Enrollment, id, "enrollment_id")
            if not enrollment:
                return JsonResponse({"error": "Enrollment not found"}, status=404)
            
            body = json.loads(request.body)
            enrollment.enrollment_id = int(body.get("enrollment_id", enrollment.enrollment_id))
            enrollment.student_name = body.get("student_name", enrollment.student_name)
            enrollment.course_name = body.get("course_name", enrollment.course_name)
            enrollment.enrollment_date = body.get("enrollment_date", enrollment.enrollment_date)
            enrollment.payment_status = body.get("payment_status", enrollment.payment_status)
            enrollment.course_status = body.get("course_status", enrollment.course_status)
            enrollment.save()
            return JsonResponse({"message": "Enrollment Updated Successfully"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method Not Allowed"}, status=405)

# DELETE /enrollments/delete/<id>/
@csrf_exempt
def delete_enrollment(request, id):
    if request.method == "DELETE":
        enrollment = get_object_by_id_or_field(Enrollment, id, "enrollment_id")
        if not enrollment:
            return JsonResponse({"error": "Enrollment not found"}, status=404)
        enrollment.delete()
        return JsonResponse({"message": "Enrollment Deleted Successfully"})
    return JsonResponse({"error": "Method Not Allowed"}, status=405)


# ==================== ASSIGNMENT VIEWS ====================

# GET /assignments/
def assignments(request):
    if request.method == "GET":
        data = list(Assignment.objects.values())
        return JsonResponse(data, safe=False)
    return JsonResponse({"error": "Method Not Allowed"}, status=405)

# POST /assignments/add/
@csrf_exempt
def add_assignment(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            # handle default values if marks not set or status blank
            marks_val = body.get("marks")
            marks = int(marks_val) if (marks_val is not None and str(marks_val).strip() != "" and str(marks_val) != "-") else None
            
            assignment = Assignment.objects.create(
                assignment_id=int(body["assignment_id"]),
                course_name=body["course_name"],
                student_name=body["student_name"],
                assignment_title=body["assignment_title"],
                submission_date=body.get("submission_date") or None,
                marks=marks,
                status=body.get("status", "Pending")
            )
            return JsonResponse({"message": "Assignment Added Successfully", "id": assignment.id})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method Not Allowed"}, status=405)

# PUT /assignments/update/<id>/
@csrf_exempt
def update_assignment(request, id):
    if request.method == "PUT":
        try:
            assignment = get_object_by_id_or_field(Assignment, id, "assignment_id")
            if not assignment:
                return JsonResponse({"error": "Assignment not found"}, status=404)
            
            body = json.loads(request.body)
            assignment.assignment_id = int(body.get("assignment_id", assignment.assignment_id))
            assignment.course_name = body.get("course_name", assignment.course_name)
            assignment.student_name = body.get("student_name", assignment.student_name)
            assignment.assignment_title = body.get("assignment_title", assignment.assignment_title)
            
            sub_date = body.get("submission_date", assignment.submission_date)
            assignment.submission_date = sub_date if sub_date else None
            
            marks_val = body.get("marks")
            if marks_val is not None:
                assignment.marks = int(marks_val) if (str(marks_val).strip() != "" and str(marks_val) != "-") else None
            
            assignment.status = body.get("status", assignment.status)
            assignment.save()
            return JsonResponse({"message": "Assignment Updated Successfully"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Method Not Allowed"}, status=405)

# DELETE /assignments/delete/<id>/
@csrf_exempt
def delete_assignment(request, id):
    if request.method == "DELETE":
        assignment = get_object_by_id_or_field(Assignment, id, "assignment_id")
        if not assignment:
            return JsonResponse({"error": "Assignment not found"}, status=404)
        assignment.delete()
        return JsonResponse({"message": "Assignment Deleted Successfully"})
    return JsonResponse({"error": "Method Not Allowed"}, status=405)
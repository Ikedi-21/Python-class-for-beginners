# COS 102 lab Pratical Assignment


name = "Nwani Chekwube Martin"
admission_year = 2025
courses = ["Python", "Mathematics", "Database", "Computer Science"]
registered_courses = ("Python", "Mathematics", "Database")
is_enrolled = True


# Q1: Student Dictionary
student = {
    "name": name,
    "admission_year": admission_year,
    "courses": courses,
    "registered_courses": registered_courses,
    "is_enrolled": is_enrolled
}
print(student)


# Q2: Custom greeting and summary
greeting = input("Enter greeting")
print(greeting, ":", student["name"], "Enrolled status:", student["is_enrolled"])


# Q3: Name and admission year
print("Name:", student["name"])
print("Admission Year:", student["admission_year"])


# Q4: First and last course
print("First course:", student["courses"][0])
print("Last course:", student["courses"][-1])


# Q5: Total number of courses using len()
print("Total courses:", len(student["courses"]))


# Q6: Enrollment check using if-else
if student["is_enrolled"]:
    print("The student is currently enrolled in the institution.")
else:
    print("The student is not currently enrolled.")


# Q7: Uppercase name using string method
print("Uppercase Name:", student["name"].upper())


# Q8: Variable data types using type()
print("Type of name:", type(name))
print("Type of admission_year:", type(admission_year))
print("Type of courses:", type(courses))
print("Type of registered_courses:", type(registered_courses))
print("Type of is_enrolled:", type(is_enrolled))
print("Type of student dictionary:", type(student))

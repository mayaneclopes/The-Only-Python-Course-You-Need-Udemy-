# Student Grading System
# You’re building an academic grading system.
# Tasks:
# Define a function calculate_grade(score) that:
# Returns “A” for score ≥ 90
# “B” for ≥ 75
# “C” for ≥ 60
# “D” for ≥ 40
# “F” otherwise
# Define a second function generate_student_report(name, score) that:
# Uses the first function to determine the grade.
# Returns a report string like: "Aman has scored 80 and received grade B"
# Write clean, reusable code using functions, conditions, and string formatting.

def calculate_grade(score: int) -> str:
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"
        
def generate_student_report(name: str, score: int) -> str:
    grade = calculate_grade(score)
    return f"{name} has scored {score} and received grade {grade}"

print(generate_student_report("Maria", 90))
print(generate_student_report("José", 35))
print(generate_student_report("Pedro", 55))
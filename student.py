# Create a module student.py containing functions to calculate total marks, percentage, and 
# grade. Import the module into another Python program and generate a student's result.
# def total(s1,s2,s3):
#     return s1+s2+s3
# def percent():
#     return (total/100)*100
# def grade():
#     if percent<90 and percent>80:
#         print("A")

def total(s1, s2, s3):
    return s1 + s2 + s3

def percent(s1, s2, s3):
    return (total(s1, s2, s3) / 300) * 100

def grade(per):
    if per >= 90:
        return "A"
    elif per >= 80:
        return "B"
    elif per >= 60:
        return "C"
    elif per >= 40:
        return "D"
    else:
        return "Fail"

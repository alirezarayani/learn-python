student_scores = input("Input a list of student score ").split()
highest_score = 0;
for n in range(0,len(student_scores)):
    student_scores[n]= int(student_scores[n])
    if student_scores[n]>highest_score:
        highest_score = student_scores[n]

print(f"The highest in the class is : {highest_score}")

print(max(student_scores))
student_heights = input("Input a list of student heights ").split()
sum_of_student_height=0
for n in range(0,len(student_heights)):
    student_heights[n] = int(student_heights[n])
    sum_of_student_height +=student_heights[n]
print(student_heights)
print(sum_of_student_height / len(student_heights))
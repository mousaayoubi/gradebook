last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
print(last_semester_gradebook)

#Create a subjects list
subjects = ["physics", "calculus", "poetry", "history"]
subjects.append("computer science")
print(subjects)

#Create a grades list
grades = [98, 97, 85, 88]
grades.append(100)
print(grades)

#Combines subjects and grades list using zip
gradebook = list(zip(subjects, grades))
gradebook.append(("visual arts", 93))
print(gradebook)

#Print Full Gradebook
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
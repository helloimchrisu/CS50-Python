# students = ["Hermione", "Harry", "Ron"]

#for student in students:
#    print(student) 

# for i in range(len(students)):
#    print(i + 1, students[i])


#--------------------------

#students = ["Hermione", "Harry", "Ron", "Draco"]
#houses = ["Gryffindor","Gryffindor","Gryffindor",#"Slytherin"]

#---------------------


#students = {
#    "Hermione":"Gryffindor",
#    "Harry":"Gryffindor",
#    "Ron":"Gryffiondor",
#    "Draco":"Slytherin",
#}

# print(students["Hermione"])

#for student in students:
#   print(student, students[student], sep=", ") 

#--------------------------------


students = [
    {"name":"Hermione", "house":"Gryffindor", "patronus":"Otter"},
    {"name":"Harry", "house":"Gryffindor", "patronus":"Stag"},
    {"name":"Ron", "house":"Gryffindor", "patronus":"Jack Russell terrier"},
    {"name":"Draco", "house":"Slytherin", "patronus": None}
]

for student in students: 
    print(student["name"], student["house"], student["patronus"], sep=", ")

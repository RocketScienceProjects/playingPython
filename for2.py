student = {
    "male": ["Tom", "Harry", "Rajan", "Nick"],
    "female": ["Sarah", "Clinty", "Sherly", "Dina"]
}

for gender in student.keys():
    for name in student[gender]:
        if "a" in name:
            print(name)

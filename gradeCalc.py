grades = {
    "Elektriske Kretser": "E",
    "Matte 1000": "C",
    "Programmering 1": "B",
    "Elektronikk": "A",
    "Digitalteknikk": "D",
    "Fysikk": "E",
    "Programmering 2": "",
    "Matte 2000": "B", 
    "Dynamiske Systemer": ""
}

gradeConversion = [
    ("A", 5),
    ("B", 4),
    ("C", 3),
    ("D", 2),
    ("E", 1),
    ("F", 0)
    ]

#Makes a list with numerical grades from the letter grades.
def grade_calc():
    calculation_list = []
    for i in grades.values():
        for o in gradeConversion:
            if i.upper() in o:
                calculation_list.append(o[1])
    return sum(calculation_list) / len(calculation_list)

def num_to_letter(num_grade):
    num_grade = round(num_grade)
    for i in gradeConversion:
        if num_grade in i:
            return i[0]

print(f"The numerical grade is: {grade_calc()}")
print(f"This rounds to a letter grade of: {num_to_letter(grade_calc())}")

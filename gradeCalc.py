actual_grades = {
    "Elektriske Kretser": "A",
    "Matte 1000": "C",
    "Programmering 1": "A",
    "Elektronikk": "A",
    "Digitalteknikk": "D",
    "Fysikk": "E",
    "Programmering 2": "A",
    "Matte 2000": "B", 
    "Dynamiske Systemer": ""
}

wishful_grades = {
    "Elektriske Kretser": "A",
    "Matte 1000": "C",
    "Programmering 1": "A",
    "Elektronikk": "A",
    "Digitalteknikk": "D",
    "Fysikk": "D",
    "Programmering 2": "A",
    "Matte 2000": "B", 
    "Dynamiske Systemer": "D"
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
def grade_calc(list_of_grades):
    calculation_list = []
    for i in list_of_grades.values():
        for o in gradeConversion:
            if i.upper() in o:
                calculation_list.append(o[1])
    return round(sum(calculation_list) / len(calculation_list), 3)

def num_to_letter(num_grade):
    num_grade = round(num_grade)
    for i in gradeConversion:
        if num_grade in i:
            return i[0]

print(f"The numerical grade is: {grade_calc(actual_grades)}")
print(f"This rounds to a letter grade of: {num_to_letter(grade_calc(actual_grades))}")
print()
print(f"The wishful grade is: {grade_calc(wishful_grades)}")
print(f"This rounds to a letter grade of: {num_to_letter(grade_calc(wishful_grades))}")

import csv

def compare_student_grades(file_path):
    grade_mapping = {
        (90, 100): 'A',
        (80, 89): 'B',
        (70, 79): 'C',
        (60, 69): 'D',
        (0, 59): 'F'
    }

    results = []

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            try:
                grades = [
                    float(row['Test1']),
                    float(row['Test2']),
                    float(row['Test3']),
                    float(row['Test4']),
                    float(row['Final'])
                ]

                average = sum(grades) / len(grades)
                for (lower, upper), grade in grade_mapping.items():
                    if lower <= average <= upper:
                        calculated_grade = grade
                        break

                actual_grade = row['Grade']
                results.append({
                    'Calculated Grade': calculated_grade,
                    'Actual Grade': actual_grade,
                    'Match': calculated_grade == actual_grade
                })

            except (ValueError, KeyError):
                continue
    return results
import pytest
from csv_handler import compare_student_grades

grade_mapping = {
    (90, 100): 'A',
    (80, 89): 'B',
    (70, 79): 'C',
    (60, 69): 'D',
    (0, 59): 'F'
}

def test_compare_student_grades():
    results = compare_student_grades('grades.csv')
    for result in results:
        assert result['Calculated Grade'] == result['Actual Grade'], (
            f"Ошибка для ученика: "
            f"Рассчитанная оценка '{result['Calculated Grade']}' "
            f"не совпадает с указанной '{result['Actual Grade']}'"
        )

def test_student_averages():
    results = compare_student_grades('grades.csv')
    for result in results:
        average = result['Average']
        calculated_grade = None
        for (lower, upper), grade in grade_mapping.items():
            if lower <= average <= upper:
                calculated_grade = grade
                break
        assert calculated_grade == result['Actual Grade'], (
            f"Ошибка для ученика: "
            f"Среднее арифметическое {average:.2f} соответствует оценке '{calculated_grade}', "
            f"но указанная оценка '{result['Actual Grade']}'"
        )
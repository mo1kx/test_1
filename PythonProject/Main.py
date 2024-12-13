from csv_handler import compare_student_grades
from json_handler import add_superheroes, check_superheroes_age


def main():
    print("Сравнение рассчитанных оценок с указанными в файле:")
    results = compare_student_grades('grades.csv')

    for i, result in enumerate(results, start=1):
        print(f"Ученик {i}: "
              f"Рассчитанная оценка = {result['Calculated Grade']}, "
              f"Указанная оценка = {result['Actual Grade']}, "
              f"Совпадение = {result['Match']}")

    print("\nЗадача 2: Работа с JSON файлом")
    new_heroes = [
        {"name": "Spider-Man", "age": 25},
        {"name": "Iron Man", "age": 48}
    ]
    add_superheroes('SuperHero.json', new_heroes)
    print("Супергерои добавлены и отсортированы по возрасту в superhero_new.json")

    result = check_superheroes_age('superhero_new.json')
    if result:
        print("Все супергерои старше 30 лет.")
    else:
        print("Не все супергерои старше 30 лет.")


if __name__ == "__main__":
    main()
import json

def add_superheroes(file_path, new_heroes):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    data['members'].extend(new_heroes)

    data['members'].sort(key=lambda x: x['age'])

    with open('superhero_new.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def check_superheroes_age(file_path):

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for hero in data['members']:
        if hero['age'] <= 30:
            return False
    return True
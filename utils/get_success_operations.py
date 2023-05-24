import json


def success_operations(path):
    """ возвращает список с успешными операциями """
    try:
        with open(path, "r", encoding='utf-8') as file:
            operations = json.load(file)  # файл с операциями
    except (FileNotFoundError, IOError):
        print("Ошибка при открытии файла")
        return []
    success = []  # список с успешными операциями
    for operation in operations:  # добавляем в пустой список словари с успешными операциями
        state = operation.get('state')
        if state == 'EXECUTED':
            success.append(operation)
    return success

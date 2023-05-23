import json


# def get_list_operation(path):
#     """ возвращает список с успешными операциями """
#     with open(path, "r", encoding='utf-8') as file:
#         list_operation = json.load(file)  # Загружаем файл операций
#
#         list_exe_op = []  # пустой список для словарей EXECUTED
#
#         for position in list_operation:
#             # перебираем словари и складываем в пустой список словари операций со статусом EXECUTED
#             try:
#                 if position['state'] == 'EXECUTED':
#                     list_exe_op.append(position)
#
#             except KeyError:
#                 continue
#
#         return list_exe_op  # возвращаем список словарей со статусом EXECUTED


def success_operations(path):
    """ возвращает список с успешными операциями """
    try:
        with open(path, "r", encoding='utf-8') as file:
            operations = json.load(file)  # файл с операциями
    except (FileNotFoundError, IOError):
        print("Ошибка при открытии файла")
        return []
    success = []  # список с успешными операциями
    for operation in operations:  # складываем в пустой список словари с успешными операциями
        state = operation.get('state')
        if state == 'EXECUTED':
            success.append(operation)
    return success

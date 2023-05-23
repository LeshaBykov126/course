from get_list_func import success_operations
from list_sort_date import last_five_operations
from change import Change

# Ссылка на файл с операциями
PATH_TO_FILE = '../operations.json'


def main():
    success = success_operations(PATH_TO_FILE)  # успешные операции
    five_last_operation = last_five_operations(success)  # список из 5 последних операций
    sort_operations = sorted(five_last_operation, key=lambda x: x['date'])  # сортируем список по дате

    # перебираем список
    for list_t in reversed(sort_operations):
        try:
            # Вызываем класс Change для изменения формата даты и обработки номеров карт и счетов
            work_class = Change(date=list_t['date'], from_whom=list_t['from'], to_whom=list_t['to'])
            print(work_class.change_date(), list_t['description'])
            print(work_class.change_from_operation(), '--->', work_class.change_to_operation())
            print(list_t['operationAmount']['amount'], list_t['operationAmount']['currency']['name'], '\n')
        # обработка ошибки
        except KeyError:
            work_class = Change(date=list_t['date'], to_whom=list_t['to'])
            print(work_class.change_date(), list_t['description'])
            print('none', '--->', work_class.change_to_operation())
            print(list_t['operationAmount']['amount'], list_t['operationAmount']['currency']['name'], '\n')


if __name__ == '__main__':
    main()

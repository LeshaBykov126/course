from change import Change
from date_operations import last_five_operations
from get_success_operations import success_operations


def main():
    success = success_operations('../operations.json')  # успешные операции
    five_last_operation = last_five_operations(success)  # список из 5 последних операций
    sort_operations = sorted(five_last_operation, key=lambda x: x['date'])  # сортируем список по дате
    for data in reversed(sort_operations):
        try:
            # данные операции (дата, ото кого, кому)
            operation_data = Change(date=data['date'], from_whom=data['from'], to_whom=data['to'])
            print(operation_data.change_date_format(), data['description'])  # меняем формат даты
            print(operation_data.change_from_operation(), '--->', operation_data.change_to_operation())
            print(data['operationAmount']['amount'], data['operationAmount']['currency']['name'], '\n')
        except KeyError:
            error = Change(date=data['date'], to_whom=data['to'])
            print(error.change_date_format(), data['description'])
            print('none', '--->', error.change_to_operation())
            print(data['operationAmount']['amount'], data['operationAmount']['currency']['name'], '\n')


if __name__ == '__main__':
    main()

def last_five_operations(file):
    """ список дат последних подтвержденных операций """
    dates = []  # пустой список для сбора дат операций
    for date in file:
        dates.append(date['date'])  # добавляем даты в список list_date
    sort_date = sorted(dates)  # сортировка дат в порядке возрастания
    last_five_dates = (sort_date[-5:])  # последние пять дат
    last_five_operations = []  # последние пять операций
    for operations in file:  # получаем операции с датами
        if operations['date'] in last_five_dates:
            last_five_operations.append(operations)
    return last_five_operations

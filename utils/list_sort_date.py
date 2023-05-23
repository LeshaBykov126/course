def last_five_operations(list_all):
    """ список дат последних подтвержденных операций """
    list_date = []  # пустой список для сбора дат операций
    for date in list_all:
        list_date.append(date['date'])  # добавляем даты в список list_date
    sorted_dates = sorted(list_date)  # Сортируем список list_date в порядке возрастания дат
    # list_date.sort()
    five_list_date = (sorted_dates[-5:])  # создаем список из последних пяти дат
    five_list_oprations = []  # пустой список для сбора пяти последних операций
    for date_key in list_all:
        # перебираем список операций и складываем нужные операции в список
        if date_key['date'] in five_list_date:
            five_list_oprations.append(date_key)
    return five_list_oprations  # Возвращаем список с 5 последними успешными операциями

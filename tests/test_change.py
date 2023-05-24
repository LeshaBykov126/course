from utils.change import Change


def test_Change():
    data_operation = Change(date="2018-04-04T17:33:34.701093", from_whom="Visa Gold 5999414228426353",
                            to_whom="Счет 90424923579946435907")
    assert data_operation.change_date_format() == '04.04.2018'
    assert data_operation.change_from_operation() == 'Visa Gold 5999 41XX XXXX 6353'
    assert data_operation.change_to_operation() == 'Счет XX5907'
    assert data_operation.__repr__() == f'Change\n' \
                                        f'Дата = 2018-04-04T17:33:34.701093\n' \
                                        f'Операция от кого = Visa Gold 5999414228426353\n' \
                                        f'Операция кому = Счет 90424923579946435907'

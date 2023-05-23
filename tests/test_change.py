from utils.change import Change

def test_Change():

    work_class = Change(date="2018-07-11T02:26:18.671407", from_operation="Visa Gold 5999414228426353", to_operation="Счет 72731966109147704472")

    assert work_class.change_date() == '11.07.2018'
    assert work_class.change_from_operation() == 'Visa Gold 5999 41XX XXXX 6353'
    assert work_class.change_to_operation() == 'Счет XX4472'

    assert work_class.__repr__() == f'Change\n' \
                                              f'Дата = 2018-07-11T02:26:18.671407\n' \
                                              f'Операция от кого = Visa Gold 5999414228426353\n' \
                                              f'Операция кому = Счет 72731966109147704472'

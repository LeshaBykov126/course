from utils.date_operations import last_five_operations


def test_last_five_operations():
    operations = [
        {'id': 587085106, 'state': 'EXECUTED', 'date': '2018-03-23T10:45:06.972075',
         'operationAmount': {'amount': '48223.05', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Открытие вклада', 'to': 'Счет 41421565395219882431'},
        {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
         'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542',
         'to': 'Счет 75651667383060284188'},
        {'id': 873106923, 'state': 'EXECUTED', 'date': '2019-03-23T01:09:46.296404',
         'operationAmount': {'amount': '43318.34', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Перевод со счета на счет', 'from': 'Счет 44812258784861134719',
         'to': 'Счет 74489636417521191160'},
        {'id': 214024827, 'state': 'EXECUTED', 'date': '2018-12-20T16:43:26.929246',
         'operationAmount': {'amount': '70946.18', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод организации', 'from': 'Счет 10848359769870775355', 'to': 'Счет 21969751544412966366'},
        {'id': 522357576, 'state': 'EXECUTED', 'date': '2019-07-12T20:41:47.882230',
         'operationAmount': {'amount': '51463.70', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод организации', 'from': 'Счет 48894435694657014368', 'to': 'Счет 38976430693692818358'},
        {'id': 895315941, 'state': 'EXECUTED', 'date': '2018-08-19T04:27:37.904916',
         'operationAmount': {'amount': '56883.54', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод с карты на карту', 'from': 'Visa Classic 6831982476737658',
         'to': 'Visa Platinum 3271587497628244'},
        {'id': 530891012, 'state': 'EXECUTED', 'date': '2019-07-11T09:15:16.739782',
         'operationAmount': {'amount': '28850.22', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Открытие вклада', 'to': 'Счет 43901232166552494845'},
        {'id': 212421010, 'state': 'EXECUTED', 'date': '2019-07-12T20:41:47.882230',
         'operationAmount': {'amount': '74591.28', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Открытие вклада', 'to': 'Счет 63278388672993234969'},
        {'id': 960011564, 'state': 'EXECUTED', 'date': '2019-02-10T09:57:36.636188',
         'operationAmount': {'amount': '46719.12', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Перевод организации', 'from': 'Счет 22786513232435358303', 'to': 'Счет 93425027635283973939'},
        {'id': 434714364, 'state': 'EXECUTED', 'date': '2019-07-09T15:28:29.786460',
         'operationAmount': {'amount': '26212.86', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод со счета на счет', 'from': 'Счет 32240557275923188435',
         'to': 'Счет 57059726131875925395'},
        {'id': 123242406, 'state': 'EXECUTED', 'date': '2018-09-14T12:40:24.860697',
         'operationAmount': {'amount': '75091.16', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод с карты на карту', 'from': 'MasterCard Gold 5229768702184183',
         'to': 'MasterCard Platinum 7344396894081384'}
    ]

    result = last_five_operations(operations)
    expected_result = [
        '2019-07-12T20:41:47.882230',
        '2019-04-04T23:20:05.206878',
        '2019-07-11T09:15:16.739782',
        '2019-07-09T15:28:29.786460'
    ]

    assert set([item['date'] for item in result]) == set(expected_result)

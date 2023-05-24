from datetime import datetime


class Change:
    def __init__(self, date='', from_whom='', to_whom=''):
        self.date = date
        self.from_whom = from_whom
        self.to_whom = to_whom

    def __repr__(self):
        return f'{self.__class__.__name__}\n' \
               f'Дата = {self.date}\n' \
               f'Операция от кого = {self.from_whom}\n' \
               f'Операция кому = {self.to_whom}'

    def change_date_format(self):
        """ функция изменения формата даты """
        change_date = datetime.strptime(self.date, '%Y-%m-%dT%H:%M:%S.%f')
        return change_date.strftime('%d.%m.%Y')

    def change_from_operation(self):
        """ функция скрывает номер карты отправителя """
        split_list = self.from_whom.split(' ')
        if len(split_list[-1]) == 16:
            split_number = split_list[-1][0:4] + ' ' + split_list[-1][4:6] + 'XX XXXX ' + split_list[-1][-4:]
            return ' '.join(split_list[:-1]) + ' ' + str(split_number)
        else:
            split_from = 'XX' + split_list[-1][-4:]
            return ' '.join(split_list[:-1]) + ' ' + str(split_from)

    def change_to_operation(self):
        """ функция скрывает номер карты получателя """
        split_list = self.to_whom.split(' ')
        if len(split_list[-1]) == 16:
            split_number = split_list[-1][0:4] + ' ' + split_list[-1][4:6] + 'XX XXXX ' + split_list[-1][-4:]
            return ' '.join(split_list[:-1]) + ' ' + str(split_number)
        else:
            split_from = 'XX' + split_list[-1][-4:]
            return ' '.join(split_list[:-1]) + ' ' + str(split_from)

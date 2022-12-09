import datetime
import unittest
from unittest.mock import patch

import app_functions
import constants


class BirthdayParadoxTestCase(unittest.TestCase):

    @patch('builtins.print')
    def test_greet_message(self, mock_print):
        app_functions.show_message(f'''Paradoks dnia urodzin.

Paradox dnia urodzin pokazuje, że w grupie N osób szanse, że dwie osoby mają urodziny w tym samym dniu, jest
zaskakująco duża. Ten program wykorzystuje metodę Monte Carlo (czyli powtarzalne, losowe symulacje), by ustalić
prawdopodobieństwo.''')

        mock_print.assert_called_with(constants.GREET_MESSAGE, end='\n')

    @patch('builtins.input', lambda _: '23')
    def test_get_amount_of_birthdays(self):
        result = app_functions.get_amount_of_birthdays()

        self.assertEqual(result, 23)

    def test_check_user_response_correct(self):
        response = '23'

        result = app_functions.check_user_response(response)

        self.assertEqual(result, True)

    def test_check_user_response_incorrect_str(self):
        response = 'abc'

        result = app_functions.check_user_response(response)

        self.assertEqual(result, False)

    def test_check_user_response_incorrect_range(self):
        response = '101'

        result = app_functions.check_user_response(response)

        self.assertEqual(result, False)

    def test_get_birthdays(self):
        start_date = datetime.date(2001, 1, 1)
        end_date = datetime.date(2001, 12, 31)
        all_dates = [start_date + datetime.timedelta(days=x) for x in range((end_date - start_date).days + 1)]
        number_of_birthdays = 100

        birthdays = app_functions.get_birthdays(number_of_birthdays)

        for birthday in birthdays:
            self.assertIn(birthday, all_dates)

    @patch('builtins.print')
    def test_show_generate_birthdays(self, mock_print):
        birthdays = [datetime.date(2001, 4, 25), datetime.date(2001, 4, 9), datetime.date(2001, 12, 10)]

        app_functions.show_generate_birthdays(birthdays)

        mock_print.assert_called_with('Kwi 25, Kwi 9, Gru 10', end='')

    def test_get_formatted_birthday_data_first_element(self):
        index = 0
        birthday = datetime.date(2001, 1, 1)
        month_name = constants.MONTHS[birthday.month - constants.SHIFT_MONTHS_INDEX]

        result = app_functions.get_formatted_birthday_data(index, birthday)

        self.assertEqual(result, f'{month_name} {birthday.day}')

    def test_get_formatted_birthday_data_second_element(self):
        index = 1
        birthday = datetime.date(2001, 1, 2)
        month_name = constants.MONTHS[birthday.month - constants.SHIFT_MONTHS_INDEX]

        result = app_functions.get_formatted_birthday_data(index, birthday)

        self.assertEqual(result, f', {month_name} {birthday.day}')


if __name__ == '__main__':
    unittest.main()

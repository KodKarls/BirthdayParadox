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

    def test_get_match_exist(self):
        birthdays = [datetime.date(2001, 4, 9), datetime.date(2001, 5, 11), datetime.date(2001, 4, 9)]

        result = app_functions.get_match(birthdays)

        self.assertEqual(result, birthdays[constants.ZERO_INDEX])

    def test_get_mach_no_exits(self):
        birthdays = [datetime.date(2001, 4, 9), datetime.date(2001, 5, 11), datetime.date(2001, 6, 17)]

        result = app_functions.get_match(birthdays)

        self.assertEqual(result, None)

    def test_get_match_message_exits(self):
        match = datetime.date(2001, 4, 9)

        result = app_functions.get_match_message(match)

        self.assertEqual(result, f'W tej sytuacji, kilka osób ma urodziny: Kwi 9.')

    def test_get_match_message_no_exits(self):
        match = None

        result = app_functions.get_match_message(match)

        self.assertEqual(result, f'W tej sytuacji, nie ma takich samych dni urodzin.')

    def test_get_simulation_match(self):
        number_of_birthdays = 23

        result = app_functions.get_simulation_match(number_of_birthdays)

        self.assertTrue(49_000 <= result <= 51_000)

    def test_check_currently_simulation_step_round(self):
        step_number = 10_000

        result = app_functions.check_currently_simulation_step(step_number)

        self.assertEqual(result, True)

    def test_check_currently_simulation_step_not_round(self):
        step_number = 10_001

        result = app_functions.check_currently_simulation_step(step_number)

        self.assertEqual(result, False)

    def test_count_probability(self):
        simulation_match = 51_550

        result = app_functions.count_probability(simulation_match)

        self.assertEqual(result, 51.55)


if __name__ == '__main__':
    unittest.main()

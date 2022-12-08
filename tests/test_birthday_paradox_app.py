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

        mock_print.assert_called_with(constants.GREET_MESSAGE)

    @patch('builtins.input', return_value='23')
    def test_get_amount_of_birthdays(self, mock_input):
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


if __name__ == '__main__':
    unittest.main()

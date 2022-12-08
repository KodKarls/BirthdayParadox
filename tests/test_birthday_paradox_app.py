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


if __name__ == '__main__':
    unittest.main()

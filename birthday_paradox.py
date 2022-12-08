import app_functions
import constants


def main() -> None:
    app_functions.show_message(constants.GREET_MESSAGE)

    amount_of_birthdays = app_functions.get_amount_of_birthdays()
    print()


if __name__ == '__main__':
    main()

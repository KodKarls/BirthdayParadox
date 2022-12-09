import app_functions
import constants


def main() -> None:
    app_functions.show_message(constants.GREET_MESSAGE)

    amount_of_birthdays = app_functions.get_amount_of_birthdays()
    app_functions.show_message()

    birthdays = app_functions.get_birthdays(amount_of_birthdays)
    app_functions.show_message(f'Oto {amount_of_birthdays} dni urodzin:')
    app_functions.show_generate_birthdays(birthdays)
    app_functions.show_message()


if __name__ == '__main__':
    main()

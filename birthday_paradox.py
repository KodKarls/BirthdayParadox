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

    match = app_functions.get_match(birthdays)
    app_functions.show_message(app_functions.get_match_message(match))

    app_functions.show_message(f'Generowanie, {amount_of_birthdays} losowych dni urodzin '
                               f'{constants.NUMBER_OF_SIMULATION} razy...')
    input(constants.INPUT_SIMULATION_PROMPT)
    simulation_match = app_functions.get_simulation_match(amount_of_birthdays)
    app_functions.show_message()

    probability = app_functions.count_probability(simulation_match)
    app_functions.show_message(f'Ze {constants.NUMBER_OF_SIMULATION} symulacji dla {amount_of_birthdays} osób, ten '
                               f'sam dzień urodzin wystąpił {simulation_match} razy.')
    app_functions.show_message(f'Oznacza to, że dla {amount_of_birthdays} ludzi istnieje {probability}% szans, iż dwie '
                               f'lub więcej osób będzie miało urodziny w tym samym dniu.')
    app_functions.show_message('To prawdopodobnie więcej, niż przypuszczałeś!')


if __name__ == '__main__':
    main()

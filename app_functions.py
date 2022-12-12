import datetime
import itertools
import random

import constants


def show_message(message: str = '', ending: str = '\n') -> None:
    print(message, end=ending)


def get_amount_of_birthdays() -> int:
    while True:
        show_message(constants.QUESTION_FOR_USER)
        response = input(constants.PROMPT_SIGN)
        if check_user_response(response):
            amount_of_birthdays = int(response)
            break

    return amount_of_birthdays


def check_user_response(response: str) -> bool:
    if response.isdecimal() and (constants.USER_RANGE_FROM <= int(response) <= constants.USER_RANGE_TO):
        return True

    return False


def get_birthdays(number_of_birthdays: int) -> list[datetime.date]:
    birthdays = []

    for i in range(number_of_birthdays):
        start_of_year = datetime.date(constants.START_YEAR, constants.START_MONTH, constants.START_DAY)
        random_number_of_days = datetime.timedelta(random.randint(constants.START_DAY_RANGE, constants.LAST_DAY_RANGE))
        birthday = start_of_year + random_number_of_days
        birthdays.append(birthday)

    return birthdays


def show_generate_birthdays(birthdays: list[datetime.date]) -> None:
    date_text = ''

    for i, birthday in enumerate(birthdays):
        date_text += get_formatted_birthday_data(i, birthday)

    show_message(date_text, '')


def get_formatted_birthday_data(index: int, birthday: datetime.date) -> str:
    result = ''

    if index != constants.ZERO_INDEX:
        result += ', '
    month_name = constants.MONTHS[birthday.month - constants.SHIFT_MONTHS_INDEX]
    result += f'{month_name} {birthday.day}'

    return result


def get_match(birthdays: list[datetime.date]) -> None | datetime.date:
    for birthday_a, birthday_b in itertools.combinations(birthdays, constants.NUMBER_OF_BIRTHDAY_COMBINATION):
        if birthday_a == birthday_b:
            return birthday_b

    return None


def get_match_message(match: None | datetime.date) -> str:
    message = constants.MATCHING_SITUATION_START_MESSAGE

    if match:
        date_text = get_formatted_birthday_data(constants.ZERO_INDEX, match)
        message += f'kilka osób ma urodziny: {date_text}.'
    else:
        message += constants.NO_MATCHING_MESSAGE

    return message

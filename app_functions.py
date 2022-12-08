import constants


def show_message(message: str) -> None:
    print(message)


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

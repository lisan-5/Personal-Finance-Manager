def validate_amount(value):
    amount = float(value)
    if amount <= 0:
        raise ValueError("Amount must be greater than 0")
    return amount

def get_user_input(prompt, validator=None):
    while True:
        try:
            value = input(prompt)
            if validator:
                value = validator(value)
            return value
        except ValueError as e:
            print(str(e))
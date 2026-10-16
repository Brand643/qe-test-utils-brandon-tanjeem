"""Validators: functions that answer yes/no. Every validator RETURNS True or False (never prints)."""


def is_in_range(value, low, high):
    """Return True if low <= value <= high (both ends included)."""
    # TODO: one comparison; Python allows low <= value <= high
    return low <= value <= high


def is_valid_test_id(test_id, prefix="TC", digits=3):
    """Return True for IDs like 'TC-007': the prefix, a dash, then exactly `digits` digits."""
    # TODO: check the start with .startswith, slice off the prefix, then .isdigit() and len()
    prefix_dash =f"{prefix}-"
    if not test_id.startswith(prefix_dash):
        return False
    id_digit = test_id[len(prefix_dash):]
    return id_digit.isdigit() and len(id_digit) == digits


def is_valid_email(email):
    """Return True for a simple email shape (a deliberately simple teaching version).

    Rules: no spaces, exactly one '@', something before the '@',
    and a domain that contains a '.' but does not start or end with one.
    """
    # TODO: early `return False` checks first (space, count of '@'), then split('@')

    # If spaces in email
    if " " in email:
        return False

    # if not exactly 1 "@"
    if not email.count("@") == 1:
        return False

    if email.startswith("@") or email.endswith("@"):
        return False

    at_sign_index = email.find("@")
    email_domain = email[at_sign_index+1:]

    if not email_domain.count(".") == 1:
        return False

    if email_domain.startswith(".") or email_domain.endswith("."):
        return False

    return True


def is_strong_password(password:str, min_length=8):
    """Return True if the password has at least `min_length` characters and
    contains at least one uppercase letter, one lowercase letter and one digit."""
    # TODO: loop over the characters with a flag per kind; .isupper() .islower() .isdigit()
    
    if len(password) < min_length:
        return False

    upper_count = 0
    lower_count = 0
    digit_count = 0

    for character in password:
        if character.isupper():
            upper_count += 1
        elif character.islower():
            lower_count += 1
        elif character.isdigit():
            digit_count += 1

    if upper_count < 1 or lower_count < 1 or digit_count < 1:
        return False

    return True


def is_valid_status_code(code):
    """Return True for HTTP status codes from 100 to 599. Reuses is_in_range."""
    # TODO: ONE line: reuse is_in_range
    return is_in_range(code, 100, 599)


def all_pass(value, *checks):
    """Return True only if EVERY check function returns a true value for `value`.

    With no checks at all, return True.
    Example: all_pass("TC-001", is_valid_test_id, lambda s: s.endswith("1"))
    """
    # TODO: loop over `checks`; return False as soon as one fails; return True after the loop
    pass

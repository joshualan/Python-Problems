"""This module contains solutions to Problem 29 of Interview Cake."""

def bracket_match(bracket):
    """Returns the matching end bracket of a start bracket"""
    if bracket == '(':
        return ')'
    if bracket == '[':
        return ']'
    if bracket == '{':
        return '}'

def bracket_validator(brackets):
    """Checks to see if a string of brackets are properly nested"""
    bracket_stack = []
    for b in brackets:
        if b == '(' or b == '{' or b == '[':
            bracket_stack.append(b)

        elif b == ')' or b == '}' or b == ']':
            top = bracket_stack.pop()

            if b != bracket_match(top):
                return False

    return True

assert bracket_validator("{ [ ] ( ) }") is True
assert bracket_validator("{ [ ( ] ) }") is False
assert bracket_validator("{ [ }") is False

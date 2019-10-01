from re import sub

# map opening brackets to corresponding closing brackets.
BRACKETS_MAP = {'(': ')', '[': ']', '{': '}'}


def is_paired(input_string: str) -> bool:
    """Return True if any and all pairs of brackets [], braces {},
    parentheses (), or any combination thereof in 'input_string'
    are matched and nested correctly; otherwise return False.
    """
    # remove non-bracket characters from 'input string'
    input_string = sub(r'[^(){}[\]]', '', input_string)

    stack = []
    for bracket in input_string:
        # if bracket is an opening bracket
        if bracket in BRACKETS_MAP:
            # push bracket to stack
            stack.append(bracket)
        # if closing bracket doesn't match corresponding opening bracket
        elif not stack or bracket != BRACKETS_MAP[stack.pop()]:
            # brackets are not balanced
            return False
    # Brackets are balanced if stack is empty
    return not stack

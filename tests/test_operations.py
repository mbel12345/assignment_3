import pytest

from typing import Union

from app.operations import Operations

# 12 total test cases for each operation.
# 3x3 = 9 cases for each non-division function, since each of the two inputs can be either 0, positive, or negative.
# 3 other cases for: positive integer with positive float, positive integer with negative float, negative float with zero.
# For division, there are 8 non-error test cases, with the 4 division-by-0 cases being put into their own test case.

Number = Union[int, float]

# addition
@pytest.mark.parametrize(
    'a, b, expected',
    [
        (2, 5, 7),
        (1, -4, -3),
        (-5, 10, 5),
        (-3, -4, -7),
        (0, 0, 0),
        (0, -4, -4),
        (-5, 0, -5),
        (0, 4, 4),
        (6, 0, 6),
        (4, 0.5, 4.5),
        (4, -0.5, 3.5),
        (-8.7, 0, -8.7),
    ],
    ids=[
        'add_positive_integers',
        'add_positive_integer_and_negative_integer',
        'add_negative_integer_and_positive_integer',
        'add_negative_integers',
        'add_zeros',
        'add_zero_and_negative_integer',
        'add_negative_integer_and_zero',
        'add_zero_and_positive_integer',
        'add_positive_integer_and_zero',
        'add_positive_integer_and_positive_float',
        'add_positive_integer_and_negative_float',
        'add_negative_float_and_zero',
    ]
)
def test_addition(a: Number, b: Number, expected: Number):

    actual = Operations.addition(a, b)
    assert actual == expected, f'Actual = {actual} does not match expected = {expected}'

# subtraction
@pytest.mark.parametrize(
    'a, b, expected',
    [
        (2, 5, -3),
        (1, -4, 5),
        (-5, 10, -15),
        (-3, -4, 1),
        (0, 0, 0),
        (0, -4, 4),
        (-5, 0, -5),
        (0, 4, -4),
        (6, 0, 6),
        (4, 0.5, 3.5),
        (4, -0.5, 4.5),
        (-8.7, 0, -8.7),
    ],
    ids=[
        'subtract_positive_integers',
        'subtract_positive_integer_and_negative_integer',
        'subtract_negative_integer_and_positive_integer',
        'subtract_negative_integers',
        'subtract_zeros',
        'subtract_zero_and_negative_integer',
        'subtract_negative_integer_and_zero',
        'subtract_zero_and_positive_integer',
        'subtract_positive_integer_and_zero',
        'subtract_positive_integer_and_positive_float',
        'subtract_positive_integer_and_negative_float',
        'subtract_negative_float_and_zero',
    ]
)
def test_subtraction(a: Number, b: Number, expected: Number):

    actual = Operations.subtraction(a, b)
    assert actual == expected, f'Actual = {actual} does not match expected = {expected}'

# multiplication
@pytest.mark.parametrize(
    'a, b, expected',
    [
        (2, 5, 10),
        (1, -4, -4),
        (-5, 10, -50),
        (-3, -4, 12),
        (0, 0, 0),
        (0, -4, 0),
        (-5, 0, 0),
        (0, 4, 0),
        (6, 0, 0),
        (4, 0.5, 2),
        (4, -0.5, -2),
        (-8.7, 0, 0),
    ],
    ids=[
        'multiply_positive_integers',
        'multiply_positive_integer_and_negative_integer',
        'multiply_negative_integer_and_positive_integer',
        'multiply_negative_integers',
        'multiply_zeros',
        'multiply_zero_and_negative_integer',
        'multiply_negative_integer_and_zero',
        'multiply_zero_and_positive_integer',
        'multiply_positive_integer_and_zero',
        'multiply_positive_integer_and_positive_float',
        'multiply_positive_integer_and_negative_float',
        'multiply_negative_float_and_zero',
    ]
)
def test_multiplication(a: Number, b: Number, expected: Number):

    actual = Operations.multiplication(a, b)
    assert actual == expected, f'Actual = {actual} does not match expected = {expected}'

# division
@pytest.mark.parametrize(
    'a, b, expected',
    [
        (2, 5, 0.4),
        (1, -4, -0.25),
        (-5, 10, -0.5),
        (-3, -4, 0.75),
        (0, -4, 0),
        (0, 4, 0),
        (4, 0.5, 8),
        (4, -0.5, -8),
    ],
    ids=[
        'divide_positive_integers',
        'divide_positive_integer_and_negative_integer',
        'divide_negative_integer_and_positive_integer',
        'divide_negative_integers',
        'divide_zero_and_negative_integer',
        'divide_zero_and_positive_integer',
        'divide_positive_integer_and_positive_float',
        'divide_positive_integer_and_negative_float',
    ]
)
def test_division_success(a: Number, b: Number, expected: Number):

    actual = Operations.division(a, b)
    assert actual == expected, f'Actual = {actual} does not match expected = {expected}'

# division by 0
@pytest.mark.parametrize(
    'a, b',
    [
        (0, 0),
        (-5, 0),
        (6, 0),
        (-8.7, 0),
    ],
    ids=[
        'divide_zero_and_zero',
        'divide_negative_integer_and_zero',
        'divide_positive_integer_and_zero',
        'divide_negative_float_and_zero',
    ]
)
def test_vision_by_zero_error(a: Number, b: Number):

    with pytest.raises(ValueError, match='Division by zero is not allowed.') as division_error:
        Operations.division(a, b)

    assert 'Division by zero is not allowed.' in str(division_error.value), f'"Division by zero is not allowed" is expected to be in error message, but error message was "{division_error.value}"'

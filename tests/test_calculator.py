import pytest
import sys

from io import StringIO

from app.calculator import Calculator

# Full testing of the operations is covered in test_operations.py.
# So, the parametrized testing here (test_calculator.py) is not intended to cover all cases, but rather demonstrate parametrized testing as a concept.
# Testing in here (test_calculator.py) is primarily for testing the REPL structure and user interactions.

def run_calc(monkeypatch, capsys, user_inputs):

    # Simulate reading input from user, and return the output from the calculator app.

    inputs = iter(user_inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    for user_input in user_inputs:
        monkeypatch.setattr(sys, 'stdin', StringIO(user_input))

    Calculator().run()

    captured = capsys.readouterr().out
    return captured

def check_result(actual, expected):

    # Check that the calculator gives a welcome message, an answer/error (expected) for user's question, and an exit message.

    actual = actual.strip().split('\n')
    assert len(actual) == 3, f'Result is expected to have 3 lines, got:\n{actual}\n{'-'*50}'
    assert actual[0] == 'Welcome to the REPL calculator!'
    assert actual[1] == expected
    assert actual[2] == 'exiting calculator'

# Tests for valid inputs

# addition
@pytest.mark.parametrize(
        'inputs, expected',
        [
            (['add 10 5', 'exit'], '15.0'),
            (['add -1 2.5', 'exit'], '1.5'),
        ],
        ids=[
            'add_positive_integer_and_positive_integer',
            'add_negative_integer_and_positive_float',
        ]
)
def test_addition(monkeypatch, capsys, inputs, expected):

    # Test addition for REPL calculator

    actual = run_calc(monkeypatch, capsys, inputs)
    check_result(actual, f'Result: {expected}')

# subtraction
@pytest.mark.parametrize(
        'inputs, expected',
        [
            (['subtract 10 5', 'exit'], '5.0'),
            (['subtract -1 2.5', 'exit'], '-3.5'),
        ],
        ids=[
            'subtract_positive_integer_and_positive_integer',
            'subtract_negative_integer_and_positive_float',
        ]
)
def test_subtraction(monkeypatch, capsys, inputs, expected):

    # Test subtraction for REPL calculator

    actual = run_calc(monkeypatch, capsys, inputs)
    check_result(actual, f'Result: {expected}')

# multiplication
@pytest.mark.parametrize(
        'inputs, expected',
        [
            (['multiply 10 5', 'exit'], '50.0'),
            (['multiply -1 2.5', 'exit'], '-2.5'),
        ],
        ids=[
            'multiply_positive_integer_and_positive_integer',
            'multiply_negative_integer_and_positive_float',
        ]
)
def test_multiplication(monkeypatch, capsys, inputs, expected):

    # Test multiplication for REPL calculator

    actual = run_calc(monkeypatch, capsys, inputs)
    check_result(actual, f'Result: {expected}')

# division
@pytest.mark.parametrize(
        'inputs, expected',
        [
            (['divide 10 5', 'exit'], '2.0'),
            (['divide -1 2.5', 'exit'], '-0.4'),
        ],
        ids=[
            'divide_positive_integer_and_positive_integer',
            'divide_negative_integer_and_positive_float',
        ]
)
def test_division(monkeypatch, capsys, inputs, expected):

    # Test division for REPL calculator

    actual = run_calc(monkeypatch, capsys, inputs)
    check_result(actual, f'Result: {expected}')

# Tests for invalid inputs

# invalid operation
@pytest.mark.parametrize(
        'inputs',
        [
            (['longdivide 9 3', 'exit']),
            (['min 4 5', 'exit']),
        ],
        ids=[
            'unknown_operation_longdivice',
            'unknown_operation_min',
        ]
)
def test_invalid_operation(monkeypatch, capsys, inputs):

    # Test invalid operation for REPL calculator

    actual = run_calc(monkeypatch, capsys, inputs)
    check_result(actual, 'Unknown operation: Please enter: add, subtract, multiply, or divide')

# wrong number of inputs
@pytest.mark.parametrize(
        'inputs',
        [
            (['add 3 4 extra-arg', 'exit']),
            (['add 4 56 5 1_extra extra-arg', 'exit']),
            (['add', 'exit']),
        ],
        ids=[
            'too_many_inputs_1_extra',
            'too_many_inputs_2_extra',
            'too_few_inputs_1_input',
        ]
)
def test_wrong_number_of_inputs(monkeypatch, capsys, inputs):

    # Test sending too may inputs to the REPL calculator
    actual = run_calc(monkeypatch, capsys, inputs)
    check_result(actual, 'Invalid input. Please follow the format: <operation> <number> <number>')

# invalid input format
@pytest.mark.parametrize(
        'inputs',
        [
            (['add two 7', 'exit']),
            (['add 4 4x', 'exit']),
        ],
        ids=[
            'invalid_format_number_spelled_out',
            'invalid_format_invalid_number',
        ]
)
def test_invalid_input_format(monkeypatch, capsys, inputs):

    # Test invalid format for REPL calculator

    actual = run_calc(monkeypatch, capsys, inputs)
    check_result(actual, 'Invalid input. Please follow the format: <operation> <number> <number>')

# division by 0
@pytest.mark.parametrize(
        'inputs',
        [
            (['divide 8 0', 'exit']),
            (['divide -5.5 0', 'exit']),
        ],
        ids=[
            'divide_positive_integer_and_zero',
            'divide_negative_float_and_zero',
        ]
)
def test_division_by_zero(monkeypatch, capsys, inputs):

    # Test division by 0 for REPL calculator

    actual = run_calc(monkeypatch, capsys, inputs)
    check_result(actual, 'Division by zero is not allowed.')

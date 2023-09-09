from etl.services.general_functions.list_evaluation_utils import (
    evaluate_and_flatten_nested_lists_with_error_handling,
)


def test_valid_input():
    """Valid input: List of strings that can be evaluated and flattened."""
    input_list = ['["apple", "banana", "cherry"]', '["date", "fig"]', '["grape"]']
    result = evaluate_and_flatten_nested_lists_with_error_handling(input_list)

    expected_result = {
        "flattened_list": ["apple", "banana", "cherry", "date", "fig", "grape"],
        "errors": [],
    }
    assert result == expected_result


def test_empty_input():
    """Valid input: Empty list should return an empty list of errors and an empty flattened list."""
    input_list = []
    result = evaluate_and_flatten_nested_lists_with_error_handling(input_list)

    expected_result = {"flattened_list": [], "errors": []}
    assert result == expected_result


def test_invalid_input():
    """Invalid input: Input contains a non-evaluable string."""
    input_list = ['["apple", "banana", "cherry"]', "invalid_syntax", '["date", "fig"]']
    result = evaluate_and_flatten_nested_lists_with_error_handling(input_list)

    expected_result = {
        "errors": [
            {"error": "name 'invalid_syntax' is not defined", "value": "invalid_syntax"}
        ],
        "flattened_list": ["apple", "banana", "cherry", "date", "fig"],
    }
    assert result == expected_result


def test_empty_string():
    """Edge case: Input contains an empty string, should be ignored with no errors."""
    input_list = ['["apple", "banana", "cherry"]', "", '["date", "fig"]']
    result = evaluate_and_flatten_nested_lists_with_error_handling(input_list)

    expected_result = {
        "flattened_list": ["apple", "banana", "cherry", "date", "fig"],
        "errors": [{"error": "invalid syntax (<string>, line 0)", "value": ""}],
    }
    assert result == expected_result


def test_single_input():
    """Valid input: Input contains only one string that can be evaluated."""
    input_list = ['["apple", "banana", "cherry"]']
    result = evaluate_and_flatten_nested_lists_with_error_handling(input_list)
    assert result == {"flattened_list": ["apple", "banana", "cherry"], "errors": []}

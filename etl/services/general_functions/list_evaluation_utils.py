def evaluate_and_flatten_nested_lists(input_string_list):
    flattened_list = []
    for value in input_string_list:
        flattened_list += eval(value)
    return flattened_list

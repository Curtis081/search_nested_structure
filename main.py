from search_nested_structure import search_nested_structure

# Example usage:
if __name__ == '__main__':
    nested_data = [
        "apple",
        ("banana", "orange"),
        {"vegetables": ["carrot", "broccoli"], "fruits": {"berry": "strawberry", "citrus": "orange"}},
        "grape"
    ]
    target_string = "strawberry"
    result = search_nested_structure(nested_data, target_string)
    if result:
        print(f"The target string '{target_string}' exists in the nested structure.")
    else:
        print(f"The target string '{target_string}' does not exist in the nested structure.")

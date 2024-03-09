import unittest

from search_nested_structure import search_nested_structure


class TestStringComparisonFunctions(unittest.TestCase):

    def test_search_nested_structure_list(self):
        """Test searching for a string in a simple list."""
        input_data = ["1", "2", "3", "4"]
        found = search_nested_structure(input_data, "3")
        self.assertTrue(found)

    def test_search_nested_structure_list_not_found(self):
        """Test searching for a string that is not in a simple list."""
        input_data = ["1", "2", "3", "4"]
        found = search_nested_structure(input_data, "5")
        self.assertFalse(found)

    def test_search_nested_structure_list_elem_not_string(self):
        """Test searching for a non-string element in a list."""
        input_data = ["1", "2", 3, "4"]
        found = search_nested_structure(input_data, 3)
        self.assertTrue(found)

    # ... (similar comments for the following test methods)
    def test_search_nested_structure_dict_not_found_a(self):
        input_data = {"a": "1", "b": {"c": "2", "d": "3"}}
        found = search_nested_structure(input_data, "a")
        self.assertFalse(found)

    def test_search_nested_structure_dict_found_1(self):
        input_data = {"a": "1", "b": {"c": "2", "d": "3"}}
        found = search_nested_structure(input_data, "1")
        self.assertTrue(found)

    def test_search_nested_structure_dict_not_found_b(self):
        input_data = ["a", "1", {"b": {"c": "2", "d": "3"}}]
        found = search_nested_structure(input_data, "b")
        self.assertFalse(found)

    def test_nested_search_nested_structure_found_3(self):
        temp_list = [{"a": 1}, [2, "3"], (4, 5)]
        self.assertTrue(search_nested_structure(temp_list, "3"))

    def test_nested_search_nested_structure_not_found_a(self):
        temp_list = [{"a": 1}, [2, "3"], (4, 5)]
        self.assertFalse(search_nested_structure(temp_list, "a"))

    def test_nested_search_nested_structure_not_found_7(self):
        temp_list = [{"a": 1}, [2, 3], (4, 5)]
        self.assertFalse(search_nested_structure(temp_list, "7"))

    def test_nested_search_nested_structure_found_strawberry(self):
        nested_data = [
            "apple",
            ("banana", "orange"),
            {"vegetables": ["carrot", "broccoli"], "fruits": {"berry": "strawberry", "citrus": "orange"}},
            "grape"
        ]
        target_string = "strawberry"
        self.assertTrue(search_nested_structure(nested_data, target_string))
        self.assertFalse(search_nested_structure(nested_data, "7"))

    def test_nested_search_nested_structure_found_apple(self):
        # ... (test data setup)
        fourth_link_list = [1, 'a', 1.5, 'bux', {1: 'c', 2: 'b'}, [1, 2, 3]]
        third_link_list = [{0: "apple"}, {'v1': ['xxx', 'yyy'], 'v2': ['test', 'ball']}, {2: 'cat'},
                         {3: ['tpp', 'ppt'], 4: ['tp', 'dis', fourth_link_list]}]
        second_link_list = ([{0: third_link_list}, {1: "dog"}, {2: "egg"}])
        first_link_list = [{0: second_link_list}, {1: "fish"}, {2: "grow"}]

        target_string = 'apple'
        self.assertTrue(search_nested_structure(first_link_list, target_string))
        self.assertFalse(search_nested_structure(first_link_list, "7"))
        self.assertFalse(search_nested_structure(first_link_list, "v2"))

        target = 3
        self.assertTrue(search_nested_structure(first_link_list, target))
        self.assertFalse(search_nested_structure(first_link_list, "yyz"))


if __name__ == '__main__':
    unittest.main()

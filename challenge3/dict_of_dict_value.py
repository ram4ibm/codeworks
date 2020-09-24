#!/usr/bin/env python
# Incomplete : 40 min

# VARIABLES
#input_nested_var   = dict(input("Enter the Nested input object: "))
#input_nested_key   = input("Enter the Nested input key: ")

#input_nested_var   = {"a": {"b": {"c": "d"}}}
input_nested_var    = {"a": {"b": {"c": {"d": "e"}}}}
#input_nested_var   = {"a": {"b": {"c": {"d": {"e": "f"}}}}}

# INITIALIZE FUNCTION VARS FOR COUNT AND ITEM
dictionary_values   = 0
count_dict_items    = input_nested_var
find_dict_item      = input_nested_var

# MAIN
# Function to get value in a key a value pair
def get_dict_value(dictionary_input):
    for (d_key, d_value) in dictionary_input.items():
        return d_value

# Function to get the total no of values
def get_dict_value_count(dictionary_input):
    if not isinstance(dictionary_input, str): # LAST VALUE wont be a dictionary
        return get_dict_value(dictionary_input)

# CALL
# STEP 1: Count Dictionary Items
while count_dict_items:
    count_dict_items = get_dict_value_count(count_dict_items)
    dictionary_values = dictionary_values + 1

# STEP 2: Find the dict item
for key_value_to_display in range( dictionary_values - 1 ):
    find_dict_item = get_dict_value(find_dict_item)
    if key_value_to_display == ( dictionary_values - 2 ): # Display the key's value
        print(find_dict_item)

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if input_list == None or len(input_list) == 0:
        return 'empty array'
    if number == '' or number is None:
        return 'Not a valid number to search'

    index = recursive_binary_search(input_list, number, 0, len(input_list) - 1)    
    return index


def recursive_binary_search(input_list, number, start_index, end_index):
    if end_index < start_index:
        return -1

    mid = (start_index + end_index)//2
    if input_list[mid] == number:
        return mid

    # if lef half is soreted
    if input_list[start_index] <= input_list[mid]:

        if number >= input_list[start_index] and number <= input_list[mid]:
            return recursive_binary_search(input_list, number, start_index, mid-1)
        return recursive_binary_search(input_list, number, mid+1, end_index)
    else: # right half is sorted
        if number >= input_list[mid] and number <= input_list[end_index]:
            return recursive_binary_search(input_list, number, mid+1, end_index)
        return recursive_binary_search(input_list, number, start_index, mid-1)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], ''))
# Nat a valid number
print(rotated_array_search([], '1'))
# empty array
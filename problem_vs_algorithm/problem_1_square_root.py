def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == '' or number is None:
        return 'Not a valid number'

    if number == 0 or number == 1:
    	return number
    square_root = 0
    array = list(range(number+1))
    square_root =  binary_search(array, number, 0, len(array)-1, square_root)
    
    return square_root
    
    
def binary_search(array, number, start_index, end_index, square_root):
	if(start_index > end_index):
		return square_root

	mid = (start_index + end_index)//2
	mid_element = array[mid]
	if mid_element * mid_element == number:
		return mid_element
	elif mid_element * mid_element > number:
		return binary_search(array, number, start_index, mid-1, mid_element)
	else:
		return binary_search(array, number, mid+1, end_index, mid_element)



print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")


print(sqrt(''))
# Not a valid number
print(sqrt(None))
# Not a valid number
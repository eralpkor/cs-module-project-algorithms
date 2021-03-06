'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# 1. Loop the array and look for doubles
# 2. Find doubles, count them and add to dictionary
# 3. Loop the dupes dictionary find the value that singled out
# First solution O(n)
def single_number(arr):
    dupes = dict()
    # Iterate over each element in list O(n)
    for i in arr:
        # If element exists in dict then increment its value else add it in dict
        if i in dupes: # O(1)
            dupes[i] += 1
        else:
            dupes[i] = 1
    # find the item that values is one
    for item, value in dupes.items():
        if value == 1:
            return item

# set() method is used to convert any of the iterable to sequence of 
# iterable elements with dintinct elements
# This is not an efficient approach but just another way to get the desired 
# results. If we add each number once and multiply the sum by 2, we will get twice 
# sum of each element of the array. Then we will subtract the sum of the whole 
# array from the twice_sum and get the required number (which appears once in the 
# array).
# 2*(sum_of_array_without_duplicates) - (sum_of_array)
def single_number2(arr):
    return 2 * sum(set(arr)) - sum(arr)


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

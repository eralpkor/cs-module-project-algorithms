'''
Input: a List of integers
Returns: a List of integers
'''
# Using list comprehension

def moving_zeroes(arr):
    return [nonZero for nonZero in arr if nonZero != 0] + \
        [zero for zero in arr if zero == 0]


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

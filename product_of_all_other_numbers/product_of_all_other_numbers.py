'''
Input: a List of integers
Returns: a List of integers
'''
# 1. Create two array prefix and suffix of length n, i.e length of the original array,
#   initialize prefix[0] = 1 and suffix[n-1] = 1 and also another array to store the result.
# 2. Traverse the array from second index to end.
# 3. For every index i update prefix[i] as prefix[i] = prefix[i-1] * array[i-1],i.e store
#   the product up-to i-1 index from the start of array.
# 4. Traverse the array from second last index to start.
# 5. For every index i update suffix[i] as suffix[i] = suffix[i+1] * array[i+1],i.e store 
#   the product up-to i+1 index from the end of array
# 6. Traverse the array from start to end.
# 7. For every index i the output will be prefix[i] * suffix[i], the product of the array 
#   element except that element.

def product_of_all_other_numbers(arr):
    n = len(arr)
     # Base case 
    if(n == 1):
        return
          
    # Allocate memory for temporary arrays left[] and right[]
    L = [0] * n
    R = [0] * n
    # Allocate memory for the result array
    result = [0] * n
    # Left most element of left array is always 1
    L[0] = 1
    # Rightmost most element of right array is always 1
    R[n - 1] = 1
    # Construct the left array
    for i in range(1, n): # [1, 1, 2]
        L[i] = arr[i - 1] * L[i - 1]

    # Construct the right array
    for j in range(n - 2, -1, -1):
        R[j] = arr[j + 1] * R[j + 1]

    # Construct the result array using
    # L[] and R[]
    for i in range(n):
        result[i] = L[i] * R[i]

    return result


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
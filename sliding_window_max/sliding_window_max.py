'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# 1. Create a nested loop, the outer loop from starting index to len(arr) – k th elements. 
#   The inner loop will run for k iterations.
# 2. Create a variable to store the maximum of k elements traversed by the inner loop.
# 3. Find the maximum of k elements traversed by the inner loop.
# 4. Print the maximum element in every iteration of outer loop

# Time Complexity: O(N * K).
# The outer loop runs n-k+1 times and the inner loop runs k times for every iteration
#  of outer loop. So time complexity is O((n-k+1)*k) which can also be written as O(N * K).
def sliding_window_max(arr, k):
    max = 0
    n = len(arr)
    result = []

    for i in range(n - k + 1):
        max = arr[i]
        for j in range(1, k):
            if arr[i + j] > max:
                max = arr[i + j]
        result.append(max)

    return result
    

# O(n)
def sliding_window_max2(arr, k):
    max = 0
    n = len(arr)
    result = []

    # max_upto array stores the index 
    # upto which the maximum element is a[i] 
    max_upto = [0 for i in range(n)]

    # Update max_upto array similar to 
    # finding next greater element
    s=[] 
    s.append(0) 
  
    for i in range(1,n): 
        while (len(s) > 0 and arr[s[-1]] < arr[i]): 
            max_upto[s[-1]] = i - 1
            del s[-1] 
          
        s.append(i) 
  
    while (len(s) > 0): 
        max_upto[s[-1]] = n - 1
        del s[-1] 
  
    j = 0
    for i in range(n - k + 1): 
  
        # j < i is to check whether the 
        # jth element is outside the window 
        while (j < i or max_upto[j] < i + k - 1): 
            j += 1
        # print(arr[j], end=" ")
        result.append(arr[j])

    return result


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
# Expected Output: [3,3,5,5,6,7] 
    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")

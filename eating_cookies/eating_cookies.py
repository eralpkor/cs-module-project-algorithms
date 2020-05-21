'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache=None):
    if not cache:
        cache = [1, 1, 2] + [0 for i in range(n - 2)]
    else:
        cache[0], cache[1], cache[2] = 1, 1, 2

    if cache[n]:
        return cache[n]
    else:
        # 1. the number of ways to first eat 3 cookies at once right now + the number of ways to eat the remaining cookies later
        # 2. the number of ways to first eat 2 cookies at once right now
        # 3. the number of ways to first eat a single cookie right now
        cache[n] = eating_cookies(n - 3, cache) \
            + eating_cookies(n - 2, cache) \
            + eating_cookies(n - 1, cache)
        return cache[n]

# 
# def eating_cookies(n, cache=None):
#     if cache is None or type(cache) == list:
#         cache = {0: 1, 1: 1, 2: 2}
#     if n not in cache:
#         cache[n] = eating_cookies(n - 3, cache) \
#             + eating_cookies(n - 2, cache) \
#             + eating_cookies(n - 1, cache)
#     return cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 3

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

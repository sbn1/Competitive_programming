#Given an integer array, partition it into two subarrays having the same sum of elements.

#Find total sum, and traverse until the toal sum minus step sum and step sum are equal

# Time: O(N)
# Spae: O(1)

def partition(arr):
    total_sum  = sum(arr)
    so_far_sum = 0

    for i in range(len(arr)):

        if so_far_sum == total_sum - so_far_sum:
            return arr[:i], arr[i:]
        so_far_sum += arr[i]
    return -1

if __name__ == "__main__":
    partition([6, -4, -3, 2, 3])
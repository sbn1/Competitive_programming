# Given an integer array between 0 and 9, find two numbers with maximum sum formed using all the array digits.
# The difference in the number of digits of the two numbers should be ± 1.

#Sort the array and select every second and turn form digits into a number
#use the reminder elements to make the second number
#Time: O(N)
# Space: O(1)

def findMaximum(arr):

    arr.sort(reverse=True)
    number_1 = 0
    number_2 = 0

    for i in range(0, len(arr),2):
        number_1 = number_1*10 + arr[i]
    for i in range(1, len(arr),2):
        number_2 = number_2*10 + arr[i]

    return number_1, number_2

if __name__ == "__main__":

    findMaximum([4, 6, 2, 7, 9, 8])
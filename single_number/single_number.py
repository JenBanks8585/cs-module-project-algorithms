'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
import random

def single_number(arr):
    num = [x for x in arr if arr.count(x) <2][0]
    return num
    

    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
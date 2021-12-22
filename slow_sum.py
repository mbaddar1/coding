    """
    https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=836241573518034&c=282010630480533&ppid=454615229006519&practice_plan=0
    Slow Sums
    Suppose we have a list of N numbers, and repeat the following operation until we're left with only a single number:
    Choose any two numbers and replace them with their sum. Moreover, we associate a penalty with each operation equal
    to the value of the new number, and call the penalty for the entire list as the sum of the penalties of each operation.
    For example, given the list [1, 2, 3, 4, 5], we could choose 2 and 3 for the first operation, which would transform the
    list into [1, 5, 4, 5] and incur a penalty of 5. The goal in this problem is to find the highest possible penalty for a
    given input.
    Signature:
    int getTotalTime(int[] arr)
    Input:
    An array arr containing N integers, denoting the numbers in the list.
    Output format:
    An int representing the highest possible total penalty.
    Constraints:
    1 ≤ N ≤ 10^6
    1 ≤ Ai ≤ 10^7, where *Ai denotes the ith initial element of an array.
    The sum of values of N over all test cases will not exceed 5 * 10^6.
    Example
    arr = [4, 2, 1, 3]
    output = 26
    First, add 4 + 3 for a penalty of 7. Now the array is [7, 2, 1]
    Add 7 + 2 for a penalty of 9. Now the array is [9, 1]
    Add 9 + 1 for a penalty of 10. The penalties sum to 26.
    """

    # Add any extra import statements you may need here


    # Add any helper functions you may need here
    import numpy as np


    def getTotalTime(arr):
        # FIXME this is nlogn runtime , can we make it n ?
        sorted_arr = sorted(arr, reverse=True)
        n = len(sorted_arr)
        if n == 0:
            return 0
        if n == 1:
            return arr[0]
        penalties = np.zeros(n) # FIXME can we make it O(1) storage
        penalties[0] = sorted_arr[0]
        for i in range(1, n):
            penalties[i] = penalties[i - 1] + sorted_arr[i]
        penalty = sum(penalties[1:])
        return penalty


    # Write your code here


    # These are the tests we use to determine if the solution is correct.
    # You can add your own at the bottom.

    def printInteger(n):
        print('[', n, ']', sep='', end='')


    test_case_number = 1


    def check(expected, output):
        global test_case_number
        result = False
        if expected == output:
            result = True
        rightTick = '\u2713'
        wrongTick = '\u2717'
        if result:
            print(rightTick, 'Test #', test_case_number, sep='')
        else:
            print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
            printInteger(expected)
            print(' Your output: ', end='')
            printInteger(output)
            print()
        test_case_number += 1


    if __name__ == "__main__":
        arr_1 = [4, 2, 1, 3]
        expected_1 = 26
        output_1 = getTotalTime(arr_1)
        check(expected_1, output_1)

        arr_2 = [2, 3, 9, 8, 4]
        expected_2 = 88
        output_2 = getTotalTime(arr_2)
        check(expected_2, output_2)

        # Add your own test cases here
        arr_2 = [3]
        expected_2 = 3
        output_2 = getTotalTime(arr_2)
        check(expected_2, output_2)

        # Add your own test cases here
        arr_2 = []
        expected_2 = 0
        output_2 = getTotalTime(arr_2)
        check(expected_2, output_2)

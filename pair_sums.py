"""
https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=840934449713537&c=282010630480533&ppid=454615229006519&practice_plan=1
"""


# Add any extra import statements you may need here


# Add any helper functions you may need here

# trick is in repeated numbers case
def numberOfWays(arr, k):
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    i = 0
    j = n - 1
    count = 0
    while j > i:
        sum_ = sorted_arr[i] + sorted_arr[j]
        if sum_ > k:
            j -= 1
        elif sum_ < k:
            i += 1
        else:
            v = sorted_arr[i]
            u = i
            while sorted_arr[u] == v and u < j:
                count += 1
                u += 1
            j -= 1
    return count


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
    k_1 = 6
    arr_1 = [1, 2, 3, 4, 3]
    expected_1 = 2
    output_1 = numberOfWays(arr_1, k_1)
    check(expected_1, output_1)

    k_2 = 6
    arr_2 = [1, 5, 3, 3, 3]
    expected_2 = 4
    output_2 = numberOfWays(arr_2, k_2)
    check(expected_2, output_2)

    k_3 = 6
    arr_3 = [1, 5, 3, 3, 3, 3]
    expected_3 = 7
    output_3 = numberOfWays(arr_3, k_3)
    check(expected_3, output_3)

    k_4 = 6
    arr_4 = [1, 5, 3, 3, 3, 3, 2, 2, 4, 4]
    expected_4 = 11
    output_4 = numberOfWays(arr_4, k_4)
    check(expected_4, output_4)

    k_5 = 6
    arr_5 = [1, 5, 3, 3, 3, 3, 2, 2, 4]
    expected_5 = 9
    output_5 = numberOfWays(arr_5, k_5)
    check(expected_5, output_5)

    # # Add your own test cases here

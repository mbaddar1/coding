"""
https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=2903692913051025&c=282010630480533&ppid=454615229006519&practice_plan=0
"""


# Add any extra import statements you may need here


# Add any helper functions you may need here


# wrong attempt
# def canGetExactChange(targetMoney, denominations):
#     denominations = sorted(denominations)
#     n = len(denominations)
#     if n == 0:
#         return False
#     leftOver = targetMoney
#     i = 0
#     while leftOver > 0 and i < n:
#         if leftOver >= denominations[i]:
#             # bills = int(leftOver / denominations[i])
#             leftOver = leftOver % denominations[i]
#         else:
#             break
#         i = i + 1
#     if np.abs(leftOver) < 1e-4:
#         return True
#     return False

#  attempt 2
def canGetExactChange(targetMoney, denominations):
    n = len(denominations)
    if n == 0:
        return False
    denominations = sorted(denominations)
    return_ = canGetExactChange_wrapper(targetMoney, denominations)
    return return_


def canGetExactChange_wrapper(targetMoney, denominations):
    n = len(denominations)
    for i in range(n - 1, -1, -1):
        if targetMoney > denominations[i]:
            new_target_money = targetMoney - denominations[i]
            return_ = canGetExactChange(new_target_money, denominations)
            if return_:
                return return_
        elif targetMoney == denominations[i]:
            return True
    return False


# Write your code here


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printString(string):
    print('[\"', string, '\"]', sep='', end='')


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
        printString(expected)
        print(' Your output: ', end='')
        printString(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    # target_1 = 94
    # arr_1 = [5, 10, 25, 100, 200]
    # expected_1 = False
    # output_1 = canGetExactChange(target_1, arr_1)
    # check(expected_1, output_1)

    target_2 = 75
    arr_2 = [4, 17, 29]
    expected_2 = True
    output_2 = canGetExactChange(target_2, arr_2)
    check(expected_2, output_2)

    # Add your own test cases here
    target_2 = 75
    arr_2 = [75]
    expected_2 = True
    output_2 = canGetExactChange(target_2, arr_2)
    check(expected_2, output_2)
    # Add your own test cases here
    target_2 = 76
    arr_2 = [75]
    expected_2 = False
    output_2 = canGetExactChange(target_2, arr_2)
    check(expected_2, output_2)
    # Add your own test cases here
    target_2 = 74
    arr_2 = [75]
    expected_2 = False
    output_2 = canGetExactChange(target_2, arr_2)
    check(expected_2, output_2)
    # Add your own test cases here
    target_2 = 50
    arr_2 = [5, 7]
    expected_2 = True
    output_2 = canGetExactChange(target_2, arr_2)
    check(expected_2, output_2)

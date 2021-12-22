"""
https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=2869293499822992&c=282010630480533&ppid=454615229006519&practice_plan=0
"""


# Add any extra import statements you may need here


# Add any helper functions you may need here
def create_val_idx_map(arr):
    n = len(arr)
    map_ = dict()
    for i in range(n):
        if arr[i] in map_.keys():
            idx_ = map_.get(arr[i])
            idx_.append(i)
            map_[arr[i]] = idx_
        else:
            map_[arr[i]] = [i]
    return map_


def is_mirror(arr_a, arr_b):
    if len(arr_a) != len(arr_b):
        return False
    if len(arr_a) == 0:
        return True
    n = len(arr_a)
    for i in range(n):
        if arr_a[i] != arr_b[n - i - 1]:
            return False
    return True


def are_they_equal_attempt1(array_a, array_b): # runtime o(n^2) memory o(1)
    if len(array_a) != len(array_b):
        return False
    if len(array_a) == 0 or len(array_a) == 1:
        return True
    n = len(array_a)
    i_a = 0
    while i_a < n:
        if array_a[i_a] == array_b[i_a]:
            i_a = i_a + 1
        else:
            i_b = n - 1  # FIXME need to optimize, can use dictionaries as hashmap
            while i_b > i_a:
                if is_mirror(array_a[i_a:i_b + 1], array_b[i_a:i_b + 1]):
                    i_a = i_b + 1
                else:
                    i_b = i_b - 1
            if i_a == i_b:
                return False
    return True


def are_they_equal(array_a, array_b): # runtime o(n) memory o(n)
    if len(array_a) != len(array_b):
        return False
    if len(array_a) == 0 or len(array_a) == 1:
        return True
    n = len(array_a)
    map_ = create_val_idx_map(array_b)
    i_a = 0

    while i_a < n:
        if array_a[i_a] == array_b[i_a]:
            i_a = i_a + 1
        else:
            if array_a[i_a] in map_.keys():
                l_ = sorted(map_.get(array_a[i_a]), reverse=True)
                for i_b in l_:
                    if i_b > i_a and is_mirror(array_a[i_a:i_b + 1], array_b[i_a:i_b + 1]):
                        i_a = i_b + 1
                        break
                    elif i_b <= i_a:
                        return False
            else:
                return False

    return True


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

    n_1 = 4
    a_1 = [1, 2, 3, 4]
    b_1 = [1, 4, 3, 2]
    expected_1 = True
    output_1 = are_they_equal(a_1, b_1)
    check(expected_1, output_1)

    n_2 = 4
    a_2 = [1, 2, 3, 4]
    b_2 = [1, 2, 3, 5]
    expected_2 = False
    output_2 = are_they_equal(a_2, b_2)
    check(expected_2, output_2)

    # Add your own test cases here

    a_3 = [1, 2, 3, 4]
    b_3 = [4, 3, 2, 1]
    expected_3 = True
    output_3 = are_they_equal(a_3, b_3)
    check(expected_3, output_3)

    # Add your own test cases here

    a_4 = []
    b_4 = []
    expected_4 = True
    output_4 = are_they_equal(a_4, b_4)
    check(expected_4, output_4)

    a_5 = []
    b_5 = [1]
    expected_5 = False
    output_5 = are_they_equal(a_5, b_5)
    check(expected_5, output_5)

    a_6 = [1, 2, 3, 4]
    b_6 = [3, 2, 1, 4]
    expected_6 = True
    output_6 = are_they_equal(a_6, b_6)
    check(expected_6, output_6)

    a_7 = [1, 2, 3, 4, 5, 6, 7]
    b_7 = [3, 2, 1, 4, 7, 6, 5]
    expected_7 = True
    output_7 = are_they_equal(a_7, b_7)
    check(expected_7, output_7)

    a_7 = [1, 2, 3, 4, 5, 6, 7]
    b_7 = [1, 3, 2, 4, 6, 5, 7]
    expected_7 = True
    output_7 = are_they_equal(a_7, b_7)
    check(expected_7, output_7)

    a_7 = [1, 1, 1]
    b_7 = [1, 1, 1]
    expected_7 = True
    output_7 = are_they_equal(a_7, b_7)
    check(expected_7, output_7)

    a_7 = [1, 2, 1, 2]
    b_7 = [2, 1, 2, 1]
    expected_7 = True
    output_7 = are_they_equal(a_7, b_7)
    check(expected_7, output_7)

    a_7 = [1, 2, 1, 1]
    b_7 = [2, 1, 1, 1]
    expected_7 = True
    output_7 = are_they_equal(a_7, b_7)
    check(expected_7, output_7)

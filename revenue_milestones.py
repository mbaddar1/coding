"""
https://www.facebookrecruiting.com/portal/coding_practice_question/?problem_id=192049171861831&c=282010630480533&ppid=454615229006519&practice_plan=0
Revenue Milestones
We keep track of the revenue Facebook makes every day, and we want to know on what days Facebook hits certain revenue milestones. Given an array of the revenue on each day, and an array of milestones Facebook wants to reach, return an array containing the days on which Facebook reached every milestone.
Signature
int[] getMilestoneDays(int[] revenues, int[] milestones)
Input
revenues is a length-N array representing how much revenue FB made on each day (from day 1 to day N). milestones is a length-K array of total revenue milestones.
Output
Return a length-K array where K_i is the day on which FB first had milestones[i] total revenue. If the milestone is never met, return -1.
Example
revenues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
milestones = [100, 200, 500]
output = [4, 6, 10]
Explanation
On days 4, 5, and 6, FB has total revenue of $100, $150, and $210 respectively. Day 6 is the first time
that FB has >= $200 of total revenue.
"""

# Add any extra import statements you may need here


# Add any helper functions you may need here
import numpy as np


def getMilestoneDays(revenues, milestones):
    milestones_idx_sort = np.argsort(milestones)  # KlogK
    n_revenues = len(revenues)
    n_milestones = len(milestones)  # K
    i_revenues = 0
    i_milestones_argsorted = 0
    cum_revenue = 0
    milestones_day_achieved = np.repeat(-1, n_milestones)
    while i_revenues < n_revenues:
        cum_revenue += revenues[i_revenues]
        while i_milestones_argsorted < n_milestones and cum_revenue >= milestones[
            milestones_idx_sort[i_milestones_argsorted]]:
            milestones_day_achieved[milestones_idx_sort[i_milestones_argsorted]] = i_revenues + 1
            i_milestones_argsorted = i_milestones_argsorted + 1
        i_revenues = i_revenues + 1
    return milestones_day_achieved


def getMilestoneDays_wrong_attempt1(revenues, milestones):
    i_revenue = 0
    i_milestones = 0
    cum_revenue = 0
    n_revenues = len(revenues)
    n_milestones = len(milestones)
    milestones_day = np.repeat(-1, n_milestones)
    while i_revenue < n_revenues:
        cum_revenue += revenues[i_revenue]
        if cum_revenue >= milestones[i_milestones]:
            milestones_day[i_milestones] = i_revenue
            i_milestones = i_milestones + 1
        i_revenue = i_revenue + 1
    return milestones_day


# Write your code here


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printIntegerList(array):
    size = len(array)
    print('[', end='')
    for i in range(size):
        if i != 0:
            print(', ', end='')
        print(array[i], end='')
    print(']', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    expected_size = len(expected)
    output_size = len(output)
    result = True
    if expected_size != output_size:
        result = False
    for i in range(min(expected_size, output_size)):
        result &= (output[i] == expected[i])
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printIntegerList(expected)
        print(' Your output: ', end='')
        printIntegerList(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    revenues_1 = [100, 200, 300, 400, 500]
    milestones_1 = [300, 800, 1000, 1400]
    expected_1 = [2, 4, 4, 5]
    output_1 = getMilestoneDays(revenues_1, milestones_1)
    check(expected_1, output_1)

    revenues_2 = [700, 800, 600, 400, 600, 700]
    milestones_2 = [3100, 2200, 800, 2100, 1000]
    expected_2 = [5, 4, 2, 3, 2]
    output_2 = getMilestoneDays(revenues_2, milestones_2)
    check(expected_2, output_2)

    # Add your own test cases here

"""
https://leetcode.com/problems/nested-list-weight-sum/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
Status
Good init solution - Get Back Later (GBL)
"""
from typing import List, Any, Union


def find_sum(a: List[Any]):
    tot_sum = 0
    for x in a:
        elem_sum = find_in_depth_sum(x,1)
        tot_sum += elem_sum
    return tot_sum
def find_in_depth_sum(b:Union[List[Any],int],depth:int) -> int:
    if isinstance(b,int):
        return depth*b
    else:
        tot_sum = 0
        for u in b:
            elem_sum = find_in_depth_sum(u,depth+1)
            tot_sum += elem_sum
        return tot_sum


if __name__ == "__main__":
    # a = [[1,1],2,[1,1]]
    # r = find_sum(a)
    # print(r)

    a = [1, [4, [6]]]
    r = find_sum(a)
    print(r)

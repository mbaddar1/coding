from typing import List


def common_prefix_two_string(str1: str, str2: str) -> str:
    n1 = len(str1)
    n2 = len(str2)
    n = min(n1,n2)
    common_prefix_res = ""
    for i in range(n):
        if str1[i] != str2[i]:
            return common_prefix_res
        common_prefix_res += str1[i]
    return common_prefix_res


def common_prefix(strings: List[str]) -> str:
    common_prefix_res = strings[0]
    n = len(strings)
    for i in range(1, n):
        common_prefix_res = common_prefix_two_string(common_prefix_res, strings[i])
        if common_prefix_res == "":
            return common_prefix_res
    return common_prefix_res


if __name__ == "__main__":
    a = ["flower", "flow", "flight"]
    comm_prefix = common_prefix(a)
    assert comm_prefix == "fl"

    strs = ["dog", "racecar", "car"]
    comm_prefix = common_prefix(strs)
    assert comm_prefix == ""

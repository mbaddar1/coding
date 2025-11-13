# https://leetcode.com/problems/basic-calculator-ii/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
from typing import Union, List, Tuple


# TODO
# Div by zero
class Solution:
    PRECEDENCE = {"*": 2, "/": 2, "+": 1, "-": 1}
    FUNC = {"+": lambda x, y: x + y, "*": lambda x, y: x * y, "/": lambda x, y: x // y, "-": lambda x, y: x - y}

    def calculate(self, s: List[List[int]]) -> int:
        n = len(s)
        elem = []
        i = 0
        while i < n:
            token, token_type, next_idx = Solution.get_next_token(i, s)
            i = next_idx
            elem.append((token, token_type))
        n_elem = len(elem)
        j = 1
        res_so_far = elem[0][0]
        while j < n_elem:
            curr_op = elem[j][0]
            next_op = elem[j + 2][0] if j + 2 < n_elem else None
            func_ = Solution.FUNC[elem[j][0]]
            if next_op and Solution.PRECEDENCE[curr_op] < Solution.PRECEDENCE[next_op]:
                res, new_idx = Solution.calculate_higher_precedence_first(idx=j + 2, elem=elem)
                res_so_far = func_(res_so_far, res)
                j = new_idx
            else:
                right_operand = elem[j + 1][0]
                res_so_far = func_(res_so_far, right_operand)
                j = j + 2
        return res_so_far

    @staticmethod
    def calculate_higher_precedence_first(idx: int, elem: List[Tuple[int, int]]) -> Tuple[int, int]:
        res = elem[idx - 1][0]
        j = idx
        while j < len(elem) and Solution.PRECEDENCE[elem[j][0]] == 2:
            func_ = Solution.FUNC[elem[j][0]]
            right_operand = elem[j + 1][0]
            res = func_(res, right_operand)
            j = j + 2

        return res,j

    # def calculate(self, s: str) -> int:
    #     i = 0
    #     n = len(s)
    #     elem = []
    #     while i < n:
    #         token, token_type, next_idx = Solution.get_next_token(i, s)
    #         i = next_idx
    #         elem.append((token, token_type))
    #     n_elem = len(elem)
    #     assert n_elem >= 3
    #     if n_elem == 3:
    #         op = elem[1][0]
    #         operand1 = elem[0][0]
    #         operand2 = elem[2][0]
    #         func_ = Solution.FUNC[op]
    #         return func_(operand1, operand2)
    #     left_operand = elem[0][0]
    #     Solution.calc_elements(left_operand=left_operand,start_idx=1,elements=elem)
    #     #
    #     # res = elem[0][0]
    #     # for j in range(1,n_elem):
    #     #     operand1 = elem[j][0]
    #     #     operand2 = elem[j+2][0]
    #     #     curr_op = elem[j+1][0]
    #     #     next_op = elem[j+3][0] if j+3 < n_elem else None
    #     #     if next_op is not None and Solution.PRECEDENCE[next_op] > Solution.PRECEDENCE[curr_op]:
    #     #         r,next_idx = Solution.flat_calc(start_idx=j+2,elem=elem)
    #     #         j = next_idx
    #     #     else:
    #     #
    #     #         res = func_(res,r)
    #     #     else:
    #     #
    #
    # @staticmethod
    # def calc_elements(left_operand: int, start_idx: int, elements: List[Tuple[int, str]]) -> Tuple[int, int]:
    #     n = len(elements)
    #     j = start_idx
    #     res_so_far = left_operand
    #     while j < n:
    #         curr_operator = elements[start_idx][0]
    #         next_operator_idx = j + 2
    #         next_operator = elements[next_operator_idx][0] if next_operator_idx < n else None
    #         if next_operator and Solution.PRECEDENCE[next_operator] > Solution.PRECEDENCE[curr_operator]:
    #             next_left_operand_idx = j + 1
    #             next_left_operand = elements[next_left_operand_idx][0]
    #             right_operand, next_idx = Solution.calc_elements(next_left_operand, next_operator_idx, elements)
    #             j = next_idx
    #             func_ = Solution.FUNC[curr_operator]
    #             res_so_far = func_(res_so_far, right_operand)
    #             return res_so_far,j
    #         else:
    #             right_operand = elements[j + 1][0]
    #             func_ = Solution.FUNC[curr_operator]
    #             res_so_far = func_(res_so_far, right_operand)
    #             j = j + 2
    #     return res_so_far, j + 2

    @staticmethod
    def calculate_expr(s: str) -> int:
        pass

    @staticmethod
    def is_numeric(c: str):
        return '0' <= c <= '9'

    @staticmethod
    def is_operator(c: str):
        return c in Solution.PRECEDENCE.keys()

    @staticmethod
    def get_next_token(index: int, s: str) -> (Union[str, int], str, int):
        n = len(s)
        if index == n:
            return "", "end", n
        finished = False
        i = index
        number = 0
        while not finished:
            if i == n:
                if number > 0:
                    return number, "number", i
                else:
                    raise ValueError("no number")
            if s[i] == ' ' or s[i] == '\t':
                pass

            if Solution.is_operator(s[i]):
                if number > 0:
                    return number, "number", i
                else:
                    return s[i], "operator", i + 1
            if Solution.is_numeric(s[i]):
                number = number * 10 + int(s[i])
            i = i + 1
        raise ValueError("impossible state")


if __name__ == '__main__':
    sol = Solution()
    s = "2*3"
    r = sol.calculate(s)
    assert r == 6

    s = "2+3"
    r = sol.calculate(s)
    assert r == 5

    s = "2+3*5"
    r = sol.calculate(s)
    assert r == 17

    s = "3+2*5+7"
    r = sol.calculate(s)
    assert r == 20

    s = "2/3+5"
    r = sol.calculate(s)
    assert r == 5

    s = "2*5+3+6+8/4"
    r = sol.calculate(s)
    assert r == 21



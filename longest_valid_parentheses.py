# https://leetcode.com/problems/longest-valid-parentheses/
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_interval = 0
        intervals = []
        stk = []
        for i, e in enumerate(s):
            if e == '(':
                stk.append((i, e))
            else:  # ')'
                if stk:
                    u = stk.pop()
                    interval = (u[0], i)
                    if intervals:
                        mergable = True
                        while intervals and mergable:
                            q = intervals.pop()
                            if interval[0] < q[0] and interval[1] > q[1]:
                                pass  # intervals.append(interval)
                            else:
                                intervals.append(q)
                                mergable = False
                        intervals.append(interval)
                    else:

                        intervals.append(interval)

        print(intervals)
        merged_intervals = []

        for j in range(len(intervals)):
            if merged_intervals:
                q = merged_intervals.pop()
                if q[1] + 1 == intervals[j][0]:
                    interval2 = (q[0], intervals[j][1])
                    merged_intervals.append(interval2)
                else:
                    merged_intervals.append(q)
                    merged_intervals.append(intervals[j])
            else:
                merged_intervals.append(intervals[j])
        print(merged_intervals)
        max_interval = 0
        for k in range(len(merged_intervals)):
            max_interval = max([max_interval, merged_intervals[k][1] - merged_intervals[k][0] + 1])
        return max_interval


if __name__ == '__main__':
    q = Solution()
    s = "()((())())"
    #s = "()(()"
    s = "(()())"
    r = q.longestValidParentheses(s)
    print(r)

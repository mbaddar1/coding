class Solution:
    def multTwoStr(self, s1, s2):

        n2 = len(s2)
        cum = 0
        for i2 in range(n2 - 1, -1, -1):
            base = 10 ** (n2 - 1 - i2)
            mult_tmp = self.auxMult(s1, s2[i2])
            cum += base * mult_tmp
        return cum

    def auxMult(self, s, c):
        n = len(s)
        cum = 0
        carry = 0
        for i in range(n - 1, -1, -1):
            base = 10 ** (n - 1 - i)
            sum_ = carry + int(s[i]) * int(c)
            carry = 1 if sum_ >= 10 else 0
            sum_ = sum_ if sum_ < 10 else sum_ - 10
            cum += sum_ * base
        return cum


if __name__ == '__main__':
    s = Solution()
    s.multTwoStr("123", "456")

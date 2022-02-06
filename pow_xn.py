"""
https://leetcode.com/explore/interview/card/facebook/54/sorting-and-searching-3/3031/
accepted
https://leetcode.com/submissions/detail/635722082/?from=explore&item_id=3031
"""
import logging
import math
import numpy as np
from tqdm import tqdm

from utils import myAssert


class Solution(object):
    def myPow(self, x, n):
        if x == 0:
            if n > 0:
                return 0
            elif n == 0:
                return np.nan
            else:  # n<0:
                return np.inf
        if n == 0:
            return 1
        sign = n / abs(n)
        n_copy = abs(n)
        acc = 1
        while n_copy >= 2:
            acc_sub = x
            log_n_abs_floor = math.floor(math.log2(abs(n_copy)))
            for _ in range(1, log_n_abs_floor + 1):
                acc_sub = acc_sub * acc_sub
            acc = acc * acc_sub
            n_copy = n_copy - (1 << log_n_abs_floor)
        if n_copy == 1:
            acc = acc * x
        if sign > 0:
            return acc
        else:
            return 1 / acc

    def myPowAttermpt1(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if abs(x) < 1e-8:
            if n > 0:
                return 0
            elif n == 0:
                return np.nan
            else:
                return np.inf
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1 / x

        if n == 2:
            return x * x
        if n == -2:
            return 1 / (x * x)
        sign = int(n / abs(n))
        n_abs = abs(n)

        log2n_abs = np.log2(n_abs)
        residual = n_abs - (1 << math.floor(log2n_abs))

        cum = x * x
        for _ in tqdm(range(2, int(log2n_abs) + 1)):
            cum = cum * cum
        for k in tqdm(range(1, residual + 1)):
            cum = cum * x
        if sign > 0:
            return cum
        else:
            return 1 / cum


if __name__ == '__main__':
    s = Solution()
    assertInst = myAssert()
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger('Main')
    # x = 5
    # n = 45
    # s.myPow(x, n)
    for i in tqdm(range(100)):
        x = np.random.randint(-100, 100)
        x=4
        if abs(x) <= 1e-8:
            continue
        pow_ = 28
        n = np.random.randint(-pow(2, pow_), pow(2, pow_) - 1)
        logger.info(f'x={x},n={n}')
        actual = s.myPow(x, n)
        # assertInst.assert_(actual=s.myPow(x, n), expected=pow(x, n))

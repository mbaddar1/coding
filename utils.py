import logging


class MyAssert:
    def __init__(self):
        self.assertion_count = 1
        self.logger = logging.getLogger(self.__class__.__name__)

    def assert_scalar(self, actual, expected):
        assert abs(actual - expected) < 1e-5, f"actual = {actual} != expected = {expected}"
        self.logger.info(f'Test # {self.assertion_count} passed!')
        self.assertion_count += 1

    def asser_in_list(self, actual, expected_list):
        assert actual in expected_list, f"actual = {actual} not in  {expected_list}"
        self.logger.info(f'Test # {self.assertion_count} passed!')
        self.assertion_count += 1

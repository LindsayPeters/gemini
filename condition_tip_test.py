import unittest

from condition_tip import conditionTip


class ConditionTipTest(unittest.TestCase):
    def test_expressions_using_high(self):
        # Given
        expressions = [
            "x is elevated",
            "x is above the normal range",
            "raised x",
            "elevated x",
            "high x"
        ]
        expected = "x is high"
        for entered in expressions:
            # When
            actual = conditionTip(entered).strip()

            # Then
            self.assertEqual(expected, actual)

    def test_expressions_using_low(self):
        # Given
        expressions = [
            "x is lowered",
            "low x",
            "x is below the normal range"
        ]
        expected = "x is low"
        for entered in expressions:
            # When
            actual = conditionTip(entered).strip()

            # Then
            self.assertEqual(expected, actual)

    def test_expressions_using_normal(self):
        # Given
        expressions = [
            "x is OK",
            "x is not high or low",
            "x is within the normal range"
        ]
        expected = "x is normal"
        for entered in expressions:
            # When
            actual = conditionTip(entered).strip()

            # Then
            self.assertEqual(expected, actual)

    def test_expressions_using_equals(self):
        # Given
        expressions = [
            ("x equals 10", "x is 10"),
            ("x is the same as y", "x is y"),
            ("x is equal to y", "x is y"),
            ("x identical to y", "x is y"),
            ("x equals \"abc\"", "x is \"abc\"")
        ]
        for entered, expected in expressions:
            # When
            actual = conditionTip(entered).strip()

            # Then
            self.assertEqual(expected, actual)

    def test_expressions_using_LTE(self):
        # Given
        expressions = [
            ("x is less than or equal to 10", "x <= 10"),
            ("x no more than y", "x <= y"),
            ("x is smaller than or equal to y", "x <= y"),
        ]
        for entered, expected in expressions:
            # When
            actual = conditionTip(entered).strip()

            # Then
            self.assertEqual(expected, actual)

    def test_expressions_using_is_in_case(self):
        # Given
        expressions = [
            "x is available",
            "there is a value for x",
            "the case contains a value for x",
            "x has been detected"

        ]
        expected = "x is in case"
        for entered in expressions:
            # When
            actual = conditionTip(entered).strip()

            # Then
            self.assertEqual(expected, actual)

    def test_expressions_using_is_increasing(self):
        # Given
        expressions = [
            "x is getting bigger",
            "increasing x",
            "x is on the rise",
            "x is going up",
            "x is rising",
            "x is increasing",
            "x is growing",
            "x is getting larger",
        ]
        expected = "x increasing"
        for entered in expressions:
            # When
            actual = conditionTip(entered).strip()

            # Then
            self.assertEqual(expected, actual)
